from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # Seeder de noticias por defecto (se ejecuta solo si la DB existe y el modelo está migrado)
        from django.db.utils import OperationalError, ProgrammingError
        from django.conf import settings
        from django.core.files import File
        import os

        try:
            from .models import Noticia

            # ✅ Borrar todas las noticias existentes
            Noticia.objects.all().delete()

            # Carpeta donde guardaste las imágenes → media/noticias/
            base_path = os.path.join(settings.MEDIA_ROOT, 'noticias')

            # ✅ Lista de noticias nuevas
            noticias = [
                {"titulo": "Counter-Strike 2 — Temporada competitiva",
                 "descripcion": "La nueva temporada de CS2 trae ajustes al sistema competitivo y balance en varias armas. Valve asegura que seguirá puliendo la experiencia.",
                 "imagen": "cs2.jpg"},

                {"titulo": "Apex Legends — Nuevo evento de colección",
                 "descripcion": "Apex recibe un evento por tiempo limitado con modos rotativos y una skin mítica exclusiva. Respawn continúa enfocándose en el matchmaking.",
                 "imagen": "apex.jpg"},

                {"titulo": "Baldur’s Gate 3 — Más nominaciones y parches",
                 "descripcion": "El RPG de Larian continúa recibiendo ajustes y balance en clases. La comunidad celebra el nivel de detalle que mantiene vivo el juego.",
                 "imagen": "baldursgate.jpg"},

                {"titulo": "Cyberpunk 2077 — Phantom Liberty impacta fuerte",
                 "descripcion": "La expansión llevó al juego a su estado definitivo. La actualización 2.0 renovó habilidades, IA y combate.",
                 "imagen": "cyberpunk.jpg"},

                {"titulo": "Death Stranding — Rumores sobre la secuela",
                 "descripcion": "Fuentes cercanas a Kojima Productions anticipan novedades en los próximos eventos. La expectativa aumenta.",
                 "imagen": "deathstranding.jpg"},

                {"titulo": "Destiny 2 — Temporada con nuevas actividades",
                 "descripcion": "Nuevas armas, misiones semanales y ajustes a la narrativa mientras se acerca el final de la saga.",
                 "imagen": "destiny2.jpg"},

                {"titulo": "Elden Ring — Expansión Shadow of the Erdtree",
                 "descripcion": "Se esperan nuevas zonas, jefes y mecánicas de combate. Los fans anticipan un desafío enorme.",
                 "descripcion": "Elden Ring sigue expandiéndose con contenido adicional que promete nuevos desafíos.",
                 "imagen": "eldenring.jpg"},

                {"titulo": "GTA V — Actualización online semanal",
                 "descripcion": "Rockstar continúa manteniendo GTA Online con eventos y misiones nuevas cada semana.",
                 "imagen": "gtav.jpg"},

                {"titulo": "Hades — Hades II continúa en desarrollo",
                 "descripcion": "Supergiant Games confirmó avances estables en la secuela, con nueva deidad protagonista.",
                 "imagen": "hades.jpg"},

                {"titulo": "Halo Infinite — Mejoras en modo Forja",
                 "descripcion": "Los jugadores reciben nuevas herramientas creativas y opciones de mapas personalizados.",
                 "imagen": "halo_infinite.jpg"},

                {"titulo": "Hogwarts Legacy — Nuevos retos para exploradores",
                 "descripcion": "Mejoras de rendimiento y cosméticos nuevos llegan al mundo mágico.",
                 "imagen": "hogleg.jpg"},

                {"titulo": "Hollow Knight — Expectativas por Silksong",
                 "descripcion": "La comunidad continúa esperando novedades, mientras el original sigue siendo referencia del género.",
                 "imagen": "HollowKnight.jpg"},

                {"titulo": "Red Dead Redemption 2 — Comunidad mod activa",
                 "descripcion": "Mientras Rockstar avanza en GTA VI, los fans mantienen RDR2 vivo con expansiones creadas por modders.",
                 "imagen": "rdr2.jpg"},

                {"titulo": "The Witcher 3 — Edición Next-Gen pulida",
                 "descripcion": "CDPR lanzó mejoras de rendimiento y texturas, manteniendo vivo uno de los RPG más influyentes.",
                 "imagen": "witcher3.jpg"},
            ]

            # Insertar noticias una por una
            for data in noticias:
                noticia = Noticia(titulo=data["titulo"], descripcion=data["descripcion"])
                imagen_path = os.path.join(base_path, data["imagen"])

                if os.path.exists(imagen_path):
                    # No copiar ni duplicar imágenes:
                    noticia.imagen = f"noticias/{data['imagen']}"
                    noticia.save()
                else:
                    noticia.save()

        except (OperationalError, ProgrammingError):
            # Si las tablas no existen aún, no rompe el arranque
            pass
