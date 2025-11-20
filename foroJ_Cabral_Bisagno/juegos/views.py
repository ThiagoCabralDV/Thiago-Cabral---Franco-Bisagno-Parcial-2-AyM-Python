from django.shortcuts import render, get_object_or_404
from .models import Juego

def juegos_view(request):
    juegos = Juego.objects.all()
    estrellas = [1,2,3,4,5]
    return render(request, "juegos/juegos.html", {"juegos": juegos, "estrellas": estrellas})

def juego_detalle(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    resenas = juego.resenas.all()  # gracias al related_name

    return render(request, "juegos/juego_detalle.html", {
        "juego": juego,
        "resenas": resenas
    })