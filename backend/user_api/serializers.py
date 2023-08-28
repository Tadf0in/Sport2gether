from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import AppUser, Sport


user_model = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['username', 'password']

    def create(self, infos):
        print(infos)
        new_user = user_model.objects.create_user(
            username = infos['username'], 
            email = infos['username'], 
            password = infos['password'],
            )
        new_user.save()

        new_appuser = AppUser()
        new_appuser.user_id = new_user       
        new_appuser.age = int(infos['age'])
        new_appuser.sexe = infos['sexe']
        new_appuser.ville = infos['ville']

        new_appuser.objectif_court_terme = infos['obj_court']
        new_appuser.objectif_long_terme = infos['obj_long']
        new_appuser.plus_gros_defi_releve = infos['defi']
        new_appuser.frequence_entrainement = infos['frequence']

        new_appuser.save()        
        
        # new_user.first_name = infos['first_name']
        # new_user.last_name = infos['last_name']
        # new_appuser.sexe = infos['sexe']
        # new_appuser.tel = infos['tel']

        # new_appuser.frequence_entrainement = infos['frequence_entrainement']
        # new_appuser.objectif_court_terme = infos['objectif_court_terme']
        # new_appuser.objectif_long_terme = infos['objectif_long_terme']
        # new_appuser.plus_gros_defi_releve = infos['plus_gros_defi_releve']

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

        
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'