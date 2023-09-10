from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from django.contrib.auth import login, logout, get_user_model

from .models import AppUser, FriendRequest
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, FriendsSerializer, FriendRequestsSerializer

user_model = get_user_model()

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
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
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    

class FriendsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        friends = AppUser.objects.get(user=request.user).get_friends()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FriendRequestsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        requests = FriendRequest.objects.filter(from_user=request.user)
        serializer = FriendRequestsSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):     
        # from_user = AppUser.objects.filter(user__username=request.data['from_user'])
        # from_user = request.user
        # to_user = user_model.objects.get(username=request.data['to_user'])

        # infos = {
        #     'from_user': from_user,
        #     'to_user': to_user
        # }

        # serializer = FriendRequestsSerializer(data=infos)
        # if serializer.is_valid(raise_exception=True):
        #     new_request = serializer.create(infos)  
            # if new_request is not None:
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)