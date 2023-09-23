from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import empty
from .models import *

user_model = get_user_model()


class PostsSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Post
        fields = ['id', 'title']

class PostSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Post
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Comment
        fields = '__all__'