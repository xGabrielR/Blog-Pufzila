from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'date', 'published',)
    list_editable = ('published',)
    list_display_links = ('name', 'email',)
