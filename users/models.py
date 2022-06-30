from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
  cep = models.CharField(blank=True, null=True, max_length=10)
  endereco = models.CharField(blank=True, null=True, max_length=250)
  numero = models.IntegerField(blank=True, null=True)
  complemento = models.CharField(blank=True, null=True, max_length=150)
  bairro = models.CharField(blank=True, null=True, max_length=150)
  cidade = models.CharField(blank=True, null=True, max_length=150)
  estado = models.CharField(blank=True, null=True, max_length=50)
  celular = models.CharField(blank=True, null=True, max_length=15)