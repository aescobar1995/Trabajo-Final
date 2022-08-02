from django.db import models

class Serie(models.Model):
    codserie = models.CharField(max_length=25, null=True, blank=True, default=None)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30)
    plataforma = models.CharField(max_length=30)
    fecha = models.DateField(default=2000)
    episodio = models.IntegerField()
    temporada = models.IntegerField()
    terminada = models.BooleanField(null=True, blank=True, default=False)
    sinopsis = models.TextField()
    imagen=models.ImageField(upload_to = 'series', null=True, blank=True)

 
    def __str__(self):
        return f"{self.codserie} || {self.nombre} "
