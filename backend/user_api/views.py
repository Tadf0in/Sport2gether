from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from django.contrib.auth import login, logout
from django.db.models import Q

from .models import Friendship
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, FriendsSerializer


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        data = request.data 

        ### validation

        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(data)
            if user is not None:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
            
		# assert validate_email(data)
		# assert validate_password(data)
        
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
     
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
     
    def get(self, request):
        serializer = UserSerializer(request.user)
        print(serializer)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    

class FriendsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        user_friends = Friendship.objects.filter(user1=request.user)
        
        reciproque = []
        for friend in user_friends:
            check = Friendship.objects.filter(user1=friend.user2, user2=request.user)
            if check.exists():
                reciproque.append(check)
        print(reciproque)

        serializer = FriendsSerializer(reciproque, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)