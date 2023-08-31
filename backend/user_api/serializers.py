from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import AppUser, Sport, FeedBack, UserSports


user_model = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ['email', 'password']

    def create(self, infos):
        new_user = user_model.objects.create_user(
            username = infos['email'], 
            email = infos['email'], 
            password = infos['password'],
            )
        new_user.save()

        new_appuser = AppUser()
        new_appuser.user_id = new_user       
        new_appuser.age = int(infos['age'])
        new_appuser.sexe = infos['gender']
        new_appuser.ville = infos['ville']

        new_appuser.objectif_court_terme = infos['obj_court']
        new_appuser.objectif_long_terme = infos['obj_long']
        new_appuser.plus_gros_defi_releve = infos['defi']
        new_appuser.frequence_entrainement = infos['frequence']

        new_appuser.save() 

        for key, value in infos['sports'].items():
            print(key, value)
            if value['checked']:
                new_usersport = UserSports()
                new_usersport.user_id = new_user
                new_usersport.sport_id = Sport.objects.get(abrev=key)
                new_usersport.save()

        if not (infos['raison'] == infos['det_raison'] ==
                infos['attente'] == infos['det_attentes'] == ''):
            new_feedback = FeedBack()
            new_feedback.user_id = new_user
            new_feedback.raison_choice = infos['raison']
            new_feedback.raisons = infos['det_raison']
            new_feedback.attente_choice = infos['attente']
            new_feedback.attentes = infos['det_attentes']
            new_feedback.save()

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