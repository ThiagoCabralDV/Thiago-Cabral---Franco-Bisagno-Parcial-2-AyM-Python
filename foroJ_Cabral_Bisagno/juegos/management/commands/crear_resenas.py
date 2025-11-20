from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from juegos.models import Juego, Reseña
import random

class Command(BaseCommand):
    help = "Genera reseñas automáticas para los juegos"

    def handle(self, *args, **kwargs):

        # Mensajes según el rating
        mensajes = {
            5: [
                "Increíble, superó todas mis expectativas.",
                "Uno de los mejores juegos que he jugado.",
                "Perfecto en todos los sentidos.",
                "Una obra maestra, cada detalle impecable.",
                "Nunca me aburrí, cada misión es épica.",
                "Gráficos y jugabilidad de otro nivel.",
                "Me encantó la historia y los personajes.",
                "Definitivamente lo volveré a jugar varias veces.",
            ],
            4: [
                "Muy bueno, aunque tiene pequeños detalles a mejorar.",
                "Disfrutable, pero esperaba algo más.",
                "Gran juego, lo recomiendo.",
                "Vale mucho la pena jugarlo.",
                "Entretenido y con buena historia.",
                "Un juego sólido aunque con algunos fallos menores.",
                "La experiencia es excelente, solo le falta un poco más.",
                "Me gustó mucho, repetiría la partida.",
            ],
            3: [
                "Está bien, pero le faltó algo.",
                "Promedio, con altibajos.",
                "Ni fu ni fa, algunos bugs molestan.",
                "No es malo, pero esperaba más.",
                "Jugable, pero podría ser mejor.",
                "Divertido a ratos, otros momentos aburrido.",
                "Una experiencia regular.",
                "No me dejó con ganas de más.",
            ],
            2: [
                "Regular, no me convenció del todo.",
                "Problemas de rendimiento y jugabilidad.",
                "No lo recomiendo mucho.",
                "Podría ser mejor.",
                "Difícil de disfrutar completamente.",
                "Muchos fallos que afectan la experiencia.",
                "La historia no me atrapó.",
                "Más frustrante que divertido.",
            ],
            1: [
                "Muy malo, no lo disfruté.",
                "Jugabilidad y gráficos pésimos.",
                "No vale la pena, decepcionante.",
                "Una experiencia frustrante.",
                "Aburrido y mal diseñado.",
                "Demasiados bugs para jugarlo.",
                "Perdí mi tiempo con este juego.",
                "No lo recomendaría a nadie.",
            ],
        }

        # Promedios deseados por juego
        promedios_deseados = {
            "Red Dead Redemption 2": 4.8,
            "The Witcher 3": 4.7,
            "Cyberpunk 2077": 4.0,
            "GTA V": 4.3,
            "Elden Ring": 4.9,
            "Counter-Strike 2": 4.5,
            "Apex Legends": 4.4,
            "Baldur’s Gate 3": 4.6,
            "Death Stranding": 4.3,
            "Destiny 2": 3.4,  # Promedio deseado ajustado
            "Hades": 4.5,
            "Halo Infinite": 4.2,
            "Hogwarts Legacy": 4.0,
            "Hollow Knight": 4.6,
        }

        usuarios = list(User.objects.all())
        juegos = Juego.objects.all()

        for juego in juegos:

            # Evitar duplicar reseñas si se ejecuta otra vez
            if juego.resenas.exists():
                continue

            cantidad_resenas = random.randint(23, 30)  # entre 23 y 30 reseñas por juego

            for _ in range(cantidad_resenas):
                usuario = random.choice(usuarios)

                # Evitar que el mismo usuario reseñe dos veces el mismo juego
                if Reseña.objects.filter(juego=juego, usuario=usuario).exists():
                    continue

                # Promedio deseado
                promedio = promedios_deseados.get(juego.titulo, 3.5)

                # Generar rating entre 1 y 5 usando random.gauss
                rating = round(random.gauss(promedio, 0.5))
                rating = max(1, min(5, rating))  # asegurar que quede entre 1 y 5

                comentario = random.choice(mensajes[rating])

                Reseña.objects.create(
                    juego=juego,
                    usuario=usuario,
                    rating=rating,
                    comentario=comentario
                )

            self.stdout.write(self.style.SUCCESS(f"{juego.titulo}: {cantidad_resenas} reseñas creadas"))
