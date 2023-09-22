from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .models import Post
from .serializers import PostsSerializer, PostSerializer


class postsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        data['post_author'] = request.user
        data['date'] += '+02:00'
        print(data)
        new_post = Post(**data)
        new_post.save()
        serializer = PostSerializer(new_post)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
  
    

