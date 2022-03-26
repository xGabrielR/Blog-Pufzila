from unicodedata import category
from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)
    list_display_links = ('id',)