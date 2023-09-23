from rest_framework import serializers
from .models import Sport
from django.contrib.auth import get_user_model

user_model = get_user_model()


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'