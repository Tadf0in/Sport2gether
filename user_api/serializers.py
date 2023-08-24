from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


user_model = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'

    def create(self, infos):
        print(infos)
        new_user = user_model.objects.create_user(
            username = infos['username'], 
            # email = infos['email'], 
            password = infos['password'],
            )
        
        # new_user.first_name = infos['first_name']
        # new_user.last_name = infos['last_name']
        # new_user.age = infos['age']
        # new_user.sexe = infos['sexe']
        # new_user.ville = infos['ville']
        # new_user.tel = infos['tel']

        # new_user.frequence_entrainement = infos['frequence_entrainement']
        # new_user.objectif_court_terme = infos['objectif_court_terme']
        # new_user.objectif_long_terme = infos['objectif_long_terme']
        # new_user.plus_gros_defi_releve = infos['plus_gros_defi_releve']

        new_user.save()
        return new_user
    

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'

    username = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, infos):      
        user = authenticate(username=infos['username'], password=infos['password'])
        if user is not None:
            return user
        else:
            raise ValidationError("login failed, user not found")
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'


        
