from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Crea 30 usuarios gamer automáticamente."

    def handle(self, *args, **kwargs):

        gamer_tags = [
            "ShadowWolf", "NeoBlade", "PixelRush", "Nighthawk", "GhostSniper",
            "ArcaneStorm", "CyberFang", "DarkNova", "LunarEcho", "RogueByte",
            "IronViper", "TurboKnight", "HexRunner", "SilentEdge", "Firestrike",
            "IceRaptor", "QuantumDash", "ZeroPulse", "OmegaRift", "SkyRaider",
            "ToxicComet", "VenomCore", "NitroFlash", "PhantomByte", "StormBreaker",
            "BladeFusion", "TeraShadow", "UltraNova", "ChaosTrigger", "DigitalSpectre"
        ]

        creados = 0

        for tag in gamer_tags:

            base_username = tag.lower()
            username = base_username

            contador = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{contador}"
                contador += 1

            User.objects.create_user(
                username=username,
                password="gaming123",
                email=f"{username}@gaminghub.com"
            )

            creados += 1

        self.stdout.write(self.style.SUCCESS(f"Usuarios gamer creados: {creados}"))
