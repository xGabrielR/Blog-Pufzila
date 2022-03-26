from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('category/<str:category>', views.PostCategory.as_view(), name='category'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='detail'),
]