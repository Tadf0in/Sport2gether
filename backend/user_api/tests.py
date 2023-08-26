from django.test import TestCase
from .models import AppUser, Sport, UserSports, FeedBack
from django.contrib.auth.models import User


class AppUserTestCase(TestCase):

    def setUp(self):
        self.test_user = User()
        self.test_user.username = "test_user"
        self.test_user.password = "T€stSetUp!23"
        self.test_user.save()

        self.test_appuser = AppUser()
        self.test_appuser.user_id = self.test_user
        self.test_appuser.age = 0
        self.test_appuser.ville = "TestVille"
        self.test_appuser.save()

        self.test_sport = Sport()
        self.test_sport.name = "Testing"
        self.test_sport.save()

    
    def test_create_appuser(self):
        nb_before = AppUser.objects.count()

        new_user = User()
        new_user.username = "tester"
        new_user.password = "T€sting!23"
        new_user.save()


        new_appuser = AppUser()
        new_appuser.user_id = new_user
        new_appuser.age = 0
        new_appuser.ville = "TestVille"
        new_appuser.save()

        nb_after = AppUser.objects.count()

        self.assertTrue(nb_after == nb_before + 1)


    def test_create_usersport(self):
        nb_before = UserSports.objects.count()

        new_usersport = UserSports()
        new_usersport.user_id = self.test_user
        new_usersport.sport_id = self.test_sport
        new_usersport.save()

        nb_after = UserSports.objects.count()

        self.assertTrue(nb_after == nb_before + 1)
        self.assertTrue(new_usersport.sport_id.name == self.test_sport.name)
        self.assertTrue(new_usersport.user_id.username == self.test_user.username)


    def test_update_appuser(self):
        pass
    

    def test_create_sport(self):
        nb_before = Sport.objects.count()

        new_sport = Sport()
        new_sport.save()

        nb_after = Sport.objects.count()

        self.assertTrue(nb_after == nb_before + 1)


    def test_delete_appuser(self):
        nb_before = AppUser.objects.count()

        self.test_appuser.delete()

        nb_after = AppUser.objects.count()

        self.assertTrue(nb_after == nb_before - 1)

    
    def test_delete_sport(self):
        nb_before = Sport.objects.count()

        self.test_sport.delete()

        nb_after = Sport.objects.count()

        self.assertTrue(nb_after == nb_before - 1)