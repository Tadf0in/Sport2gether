from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import AppUser, FriendRequest


user_model = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'

    def create(self, infos):
        new_user = user_model.objects.create_user(
            username = infos['username'], 
            email = infos['username'], 
            password = infos['password'],
            )
        new_user.save()

        new_appuser = AppUser()
        new_appuser.user = new_user       
        new_appuser.age = infos['age']
        new_appuser.ville = infos['ville']
        new_appuser.save()        
        
        # new_user.first_name = infos['first_name']
        # new_user.last_name = infos['last_name']
        # new_user.sexe = infos['sexe']
        # new_user.tel = infos['tel']

        # new_user.frequence_entrainement = infos['frequence_entrainement']
        # new_user.objectif_court_terme = infos['objectif_court_terme']
        # new_user.objectif_long_terme = infos['objectif_long_terme']
        # new_user.plus_gros_defi_releve = infos['plus_gros_defi_releve']

        return new_user
    

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'

    username = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, infos):      
        user = authenticate(username=infos['username'], password=infos['password'])
        if user is not None:
            return user
        else:
            raise ValidationError("login failed, user not found")
        

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    appuser = AppUserSerializer()

    class Meta:
        model = user_model
        fields = '__all__'


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields =  ['id', 'username']
    

class FriendRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'