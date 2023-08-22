from django.contrib import admin
from.models import AppUser, Sport, UserSports, FeedBack



@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['username', 'email']

    def username(self, au):
        return au.user_id.username
    
    def email(self, au):
        return au.user_id.email
    


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    search_fields = ['name']



@admin.register(UserSports)
class UserSportsAdmin(admin.ModelAdmin):
    list_display = ['user', 'sport']
    search_fields = ['user']
    list_filter = ['sport_id']

    def user(self, us):
        return us.user_id.username
    
    def sport(self, us):
        return us.sport_id.name



@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'raison_choice', 'attente_choice']
    search_fields = ['user']
    list_filter = ['raison_choice', 'attente_choice']


    def user(self, fb):
        return fb.user_id.username