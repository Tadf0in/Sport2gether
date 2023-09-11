from django.urls import path
from . import views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
	path('friends', views.FriendsView.as_view(), name='friends'),
    path('friends/<int:friend_pk>', views.FriendsView.as_view(), name='friend'),
	path('friends/requests', views.FriendRequestsView.as_view(), name='friendrequests'),
	path('friends/requests/<int:pk>', views.FriendRequestsView.as_view(), name='friendrequest'),
]

