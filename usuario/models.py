from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='customer_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customer_set', blank=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
