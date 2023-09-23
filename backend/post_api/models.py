from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Post(models.Model):
    post_author = models.ForeignKey(user_model, related_name="post_author", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    desc = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    posted_date = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=128)
    private = models.BooleanField()
    nb_limit = models.SmallIntegerField()
    inscrits = models.ManyToManyField(user_model, related_name="inscrits", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(user_model, related_name="comment_author", on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, editable=False)