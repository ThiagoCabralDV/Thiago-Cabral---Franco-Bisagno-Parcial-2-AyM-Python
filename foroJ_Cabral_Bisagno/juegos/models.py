from django.db import models
from django.contrib.auth.models import User

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    imagen = models.FileField(upload_to="juegos/", blank=True, null=True)

    def __str__(self):
        return self.titulo

    @property
    def rating_promedio(self):
        from django.db.models import Avg
        promedio = self.resenas.aggregate(Avg("rating"))["rating__avg"]
        return round(promedio, 1) if promedio else 0
    
class Reseña(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name="resenas")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.titulo}"