from django.urls import path
from . import views

urlpatterns = [
    path('', views.postsView.as_view(), name='posts'),
    path('<int:post_pk>', views.postView.as_view(), name='post'),
]