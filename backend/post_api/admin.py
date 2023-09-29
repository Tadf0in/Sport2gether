from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_author', 'date', 'location')
    search_fields = ('author', 'title', 'date', 'posted_date', 'location')
    list_filter = ('location', 'date', 'posted_date', 'sport')
    readonly_fields = ('posted_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_author', 'text')
    search_fields = ('post', 'author', 'comment_date')
    list_filter = ('comment_date',)
    readonly_fields = ('comment_date',)