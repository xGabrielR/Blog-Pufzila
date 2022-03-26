from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.urls import reverse

class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-Mail')
    text = models.TextField(verbose_name='Texto')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='User', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    published = models.BooleanField(default=True, verbose_name='Publicado')

    class Meta:
        verbose_name_plural = 'Comentários'
        ordering = ('-date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})