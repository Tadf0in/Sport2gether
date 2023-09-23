from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from django.contrib.auth import login, logout, get_user_model
from django.db.models import Q

from .models import AppUser, FriendRequest
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer, FriendsSerializer, FriendRequestsSerializer
from sport_api.models import Sport
from sport_api.serializers import SportSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

user_model = get_user_model()


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('email', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('password', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('first_name', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('last_name', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('age', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('gender', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('ville', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('obj_court', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('obj_long', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('defi', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('frequence', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('sports', openapi.IN_QUERY, type=openapi.TYPE_ARRAY, items=[
                openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
                openapi.Parameter('checked', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
            ]),
            openapi.Parameter('raison', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('det_raison', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('attente', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('det_attentes', openapi.IN_QUERY, type=openapi.TYPE_STRING)      
        ],
        responses={
            201:"CREATED",
            400:"BAD REQUEST",
            500:"INTERNAL ERROR ex: Username Already Exist"
        }
    )
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('password', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
        ],
        responses={
            200:"OK",
            400:"BAD REQUEST"
        }
    )
    def post(self, request):
        data = request.data
        
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    
    @swagger_auto_schema(responses={200:"OK"})
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    
    @swagger_auto_schema(responses={200:UserSerializer, 403:"FORBIDDEN"},)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class FriendsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(responses={200:FriendsSerializer, 403:"FORBIDDEN"})
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

    @swagger_auto_schema(responses={200:FriendRequestsSerializer, 403:"FORBIDDEN"})
    def get(self, request, pk=None):
        requests = FriendRequest.objects.filter(Q(from_user=request.user) | Q(to_user=request.user))
        serializer = FriendRequestsSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('to_user', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)],
        responses={200:"OK",  400:"BAD REQUEST", 403:"FORBIDDEN"}
    )
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


class UserSportsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(responses={200:SportSerializer, 403:"FORBIDDEN"})
    def get(self, request, sport_pk=None):
        sports = request.user.appuser.get_sports()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('sport_pk', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)],
        responses={200:"OK",  400:"BAD REQUEST", 403:"FORBIDDEN"}
    )
    def post(self, request, sport_pk=None):
        sport = Sport.objects.get(pk=request.data['sport_pk'])
        request.user.appuser.sports.add(sport)
        serializer = SportSerializer(sport)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, sport_pk):
        request.user.appuser.sports.remove(Sport.objects.get(pk=sport_pk))
        return Response(status=status.HTTP_200_OK)

