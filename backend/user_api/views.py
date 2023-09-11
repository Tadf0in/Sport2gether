from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response

from django.contrib.auth import login, logout, get_user_model
from django.db.models import Q

from .models import Sport, AppUser, FriendRequest
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, SportSerializer, FriendsSerializer, FriendRequestsSerializer

user_model = get_user_model()

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user is not None:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()


    def post(self, request):
        data = request.data
            
		# assert validate_email(data)
		# assert validate_password(data)
        
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        

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
 

class SportView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def get(self, request):
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     serializer = SportSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    
class FriendsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, friend_pk=None):
        friends = AppUser.objects.get(user=request.user).get_friends()
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, friend_pk):
        user = request.user
        target_user = user_model.objects.get(pk=friend_pk)
        
        user.appuser.friends.remove(target_user)
        target_user.appuser.friends.remove(request.user)

        return Response(status=status.HTTP_200_OK)
    

class FriendRequestsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, pk=None):
        requests = FriendRequest.objects.filter(Q(from_user=request.user) | Q(to_user=request.user))
        serializer = FriendRequestsSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        from_user = request.user
        to_user = user_model.objects.get(pk=request.data['to_user'])

        # Check if already friends
        if from_user in to_user.appuser.get_friends() or to_user in from_user.appuser.get_friends():
            return Response("Already friends", status=status.HTTP_400_BAD_REQUEST)
        
        # Check if reciproque request already exists 
        reciprocity = FriendRequest.objects.filter(from_user=to_user, to_user=from_user)
        if reciprocity.exists():
            from_user.appuser.friends.add(to_user)
            to_user.appuser.friends.add(from_user)
            reciprocity.delete()
            return Response("Request accepted, now friends", status=status.HTTP_201_CREATED)
        else:
            new_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
            if created:
                return Response("Request sent", status=status.HTTP_201_CREATED)
            else:
                return Response("Request already sent", status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        FriendRequest.objects.filter(from_user=request.user, pk=pk).delete()
        return Response(status=status.HTTP_200_OK)
