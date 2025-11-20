from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Juego, Reseña  # Importamos también Reseña

def juegos_view(request):
    juegos = Juego.objects.all()
    estrellas = [1, 2, 3, 4, 5]
    return render(request, "juegos/juegos.html", {
        "juegos": juegos,
        "estrellas": estrellas
    })

def juego_detalle(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    resenas = juego.resenas.all()  # gracias al related_name

    # Procesar envío de reseña solo si el usuario está autenticado
    if request.method == "POST" and request.user.is_authenticated:
        rating = int(request.POST.get("rating", 5))
        comentario = request.POST.get("comentario", "").strip()
        if comentario:  # Solo crear si hay texto
            Reseña.objects.create(
                juego=juego,
                usuario=request.user,
                rating=rating,
                comentario=comentario,
                fecha=timezone.now()
            )
            return redirect("juego_detalle", juego_id=juego.id)

    return render(request, "juegos/juego_detalle.html", {
        "juego": juego,
        "resenas": resenas
    })
