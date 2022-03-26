from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name