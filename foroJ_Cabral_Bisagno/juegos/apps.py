from django.apps import AppConfig

class JuegosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'juegos'

    def ready(self):
        from django.db.utils import OperationalError, ProgrammingError
        from django.conf import settings
        import os

        try:
            from .models import Juego

            # ❗ SI YA EXISTEN JUEGOS, NO HACEMOS NADA
            if Juego.objects.exists():
                return

            print("Cargando juegos por primera vez...")

            base_path = os.path.join(settings.MEDIA_ROOT, 'juegos')

            # 🟩 LISTA COMPLETA — mismos juegos que en noticias
            juegos = [
                {"titulo": "Counter-Strike 2", "descripcion": "Shooter competitivo táctico de Valve.", "imagen": "cs2.jpg"},
                {"titulo": "Apex Legends", "descripcion": "Battle royale frenético por escuadrones.", "imagen": "apex.jpg"},
                {"titulo": "Baldur’s Gate 3", "descripcion": "RPG basado en D&D con decisiones profundas.", "imagen": "baldursgate.jpg"},
                {"titulo": "Cyberpunk 2077", "descripcion": "RPG futurista en Night City.", "imagen": "cyberpunk.jpg"},
                {"titulo": "Death Stranding", "descripcion": "Aventura narrativa de Kojima en un mundo postapocalíptico.", "imagen": "deathstranding.jpg"},
                {"titulo": "Destiny 2", "descripcion": "Shooter-looter online con actividades semanales.", "imagen": "destiny2.jpg"},
                {"titulo": "Elden Ring", "descripcion": "Mundo abierto desafiante creado por FromSoftware.", "imagen": "eldenring.jpg"},
                {"titulo": "GTA V", "descripcion": "Acción abierta en Los Santos.", "imagen": "gtav.jpg"},
                {"titulo": "Hades", "descripcion": "Roguelike rápido ambientado en la mitología griega.", "imagen": "hades.jpg"},
                {"titulo": "Halo Infinite", "descripcion": "Shooter de ciencia ficción con modo Forja.", "imagen": "halo_infinite.jpg"},
                {"titulo": "Hogwarts Legacy", "descripcion": "Exploración mágica en el mundo de Harry Potter.", "imagen": "hogleg.jpg"},
                {"titulo": "Hollow Knight", "descripcion": "Metroidvania de exploración y combate preciso.", "imagen": "HollowKnight.jpg"},
                {"titulo": "Red Dead Redemption 2", "descripcion": "Western inmersivo con mundo abierto detallado.", "imagen": "rdr2.jpg"},
                {"titulo": "The Witcher 3", "descripcion": "RPG narrativo con mundo abierto enorme.", "imagen": "witcher3.jpg"},
            ]

            for data in juegos:
                juego = Juego(titulo=data["titulo"], descripcion=data["descripcion"])
                img_path = os.path.join(base_path, data["imagen"])

                if os.path.exists(img_path):
                    juego.imagen = f"juegos/{data['imagen']}"

                juego.save()

        except (OperationalError, ProgrammingError):
            # Tablas aún no creadas → no romper
            pass