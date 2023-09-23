from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# User Inline
class AppUserInline(admin.StackedInline):
    model = AppUser
    can_delete = False

class AppUserAdmin(UserAdmin):
    inlines = [AppUserInline]

    list_display = ['username', 'first_name', 'last_name', 'id']

admin.site.unregister(User)
admin.site.register(User, AppUserAdmin)



@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    search_fields = ('user__username',)
    filter_horizontal = ('friends', 'sports')

    def username(self, au):
        return au.user.username
    
    def email(self, au):
        return au.user.email


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'raison_choice', 'attente_choice']
    search_fields = ['user']
    list_filter = ['raison_choice', 'attente_choice']


    def user(self, fb):
        return fb.user.username
    

@admin.register(FriendRequest)
class FriendRequestsAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'date']
    search_fields = ['from_user', 'to_user']
    list_filter = ['date']