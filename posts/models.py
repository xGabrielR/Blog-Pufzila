from django.db import models
from django.urls import reverse
from categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    body = models.TextField(verbose_name='Texto')
    image = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Criação')
    updated = models.DateTimeField(auto_now=True, verbose_name='Atualização')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})