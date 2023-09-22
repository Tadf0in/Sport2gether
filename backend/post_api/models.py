from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Post(models.Model):
    post_author = models.ForeignKey(user_model, related_name="post_author", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    desc = models.TextField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    posted_time = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=128)
    private = models.BooleanField()
    nb_limit = models.SmallIntegerField()
    inscrits = models.ManyToManyField(user_model, related_name="inscrits", blank=True)


class Comments(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(user_model, related_name="comment_author", on_delete=models.CASCADE)
    text = models.TextField()


class 