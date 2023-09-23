from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import *
from .serializers import *


class postsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        request : {
            title: str,
            desc: str,
            date: datetime,
            location: str,
            private: bool,
            nb_limit: int
        }
        """
        data = request.data
        data['post_author'] = request.user
        data['date'] += '+02:00'
        new_post = Post(**data)
        new_post.save()
        serializer = PostSerializer(new_post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class postView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

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

    def get(self, request, post_pk):
        comments = Comment.objects.filter(post__pk=post_pk)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, post_pk):
        """
        request : {
            text: str,
        }
        """
        new_comment = Comment()
        new_comment.text = request.data['text']
        new_comment.comment_author = request.user
        new_comment.post = Post.objects.get(pk=post_pk) 
        new_comment.save()
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class commentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, post_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, post_pk, comment_pk):
        Comment.objects.filter(pk=comment_pk).delete()
        return Response(status=status.HTTP_200_OK)

  
    

