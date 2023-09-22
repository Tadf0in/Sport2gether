from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import empty
from .models import Post, Comment

user_model = get_user_model()


class PostsSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Post
        fields = ['id', 'title']

class PostSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Post
        fields = '__all__'