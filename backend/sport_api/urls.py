from django.urls import path
from . import views

urlpatterns = [
    path('', views.SportView.as_view(), name='sports')
]
