from .models import Post
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'created', 'updated', 'published')
    list_editable = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
