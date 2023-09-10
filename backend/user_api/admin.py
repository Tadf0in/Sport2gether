from django.contrib import admin
from.models import AppUser, Sport, UserSports, FeedBack, FriendRequest

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# User Inline
class AppUserInline(admin.StackedInline):
    model = AppUser
    can_delete = False

class AppUserAdmin(UserAdmin):
    inlines = [AppUserInline]

admin.site.unregister(User)
admin.site.register(User, AppUserAdmin)



@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['username', 'email']
    filter_horizontal = ('friends',)

    def username(self, au):
        return au.user.username
    
    def email(self, au):
        return au.user.email
    

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    search_fields = ['name']



@admin.register(UserSports)
class UserSportsAdmin(admin.ModelAdmin):
    list_display = ['user', 'sport']
    search_fields = ['user']
    list_filter = ['sport']

    def user(self, us):
        return us.user.username
    
    def sport(self, us):
        return us.sport.name



@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'raison_choice', 'attente_choice']
    search_fields = ['user']
    list_filter = ['raison_choice', 'attente_choice']


    def user(self, fb):
        return fb.user.username
    

@admin.register(FriendRequest)
class FriendRequestsAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user']
    search_fields = ['from_user', 'to_user']