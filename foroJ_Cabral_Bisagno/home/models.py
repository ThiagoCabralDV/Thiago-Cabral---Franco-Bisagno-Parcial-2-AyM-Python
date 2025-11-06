from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen = models.FileField(upload_to='noticias/', blank=True, null=True)  # se guarda en media/noticias/
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo