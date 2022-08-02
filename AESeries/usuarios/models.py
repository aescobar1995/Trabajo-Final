from django.db import models
from email.policy import default
from tokenize import blank_re

class Binger(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    alias = models.CharField(max_length=20)

    def __str__(self):
        return f"Binger {self.nombre} {self.apellido}"


class Critico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    alias = models.CharField(max_length=20)
    experiencia = models.TextField()

    def __str__(self):
        return f"Critico {self.nombre} {self.apellido}"
