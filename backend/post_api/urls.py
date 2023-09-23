from django.urls import path
from . import views

urlpatterns = [
    path('', views.postsView.as_view(), name='posts'),
    path('<int:post_pk>', views.postView.as_view(), name='post'),
    path('<int:post_pk>/comments', views.commentsView.as_view(), name='comments'),
    path('<int:post_pk>/comments/<int:comment_pk>', views.commentView.as_view(), name='comment'),
]