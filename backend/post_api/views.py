from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import *
from .serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class postsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(responses={200:PostsSerializer})
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('desc', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('date', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('location', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('private', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, required=True),
            openapi.Parameter('nb_limit', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('sport', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={201:"CREATED", 400:"BAD REQUEST"}
    )
    def post(self, request):
        data = request.data
        data['post_author'] = request.user.pk
        data['date'] += '+02:00'
        serializer = PostSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data['post_author'] = user_model.objects.get(pk=request.user.pk)
            data['sport'] = Sport.objects.get(pk=data['sport'])
            post = serializer.create(data)
            if post is not None:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class postView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(responses={200:PostSerializer})
    def get(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        serializer = PostSerializer(post) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, post_pk):
        Post.objects.filter(pk=post_pk).delete()
        return Response(status=status.HTTP_200_OK)
    

class commentsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(responses={200:CommentsSerializer})
    def get(self, request, post_pk):
        comments = Comment.objects.filter(post__pk=post_pk)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[openapi.Parameter('text', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)],
        responses={201:"CREATED", 400:"BAD REQUEST"}
    )
    def post(self, request, post_pk):
        new_comment = Comment()
        new_comment.text = request.data['text']
        new_comment.comment_author = request.user
        new_comment.post = Post.objects.get(pk=post_pk) 
        new_comment.save()
        serializer = CommentSerializer(new_comment)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class commentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(responses={200:CommentSerializer})
    def get(self, request, post_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, post_pk, comment_pk):
        Comment.objects.filter(pk=comment_pk).delete()
        return Response(status=status.HTTP_200_OK)

  
    

