from django.urls import path
from .views import juegos_view
from . import views

urlpatterns = [
    path('', juegos_view, name='juegos'),
    path("<int:juego_id>/", views.juego_detalle, name="juego_detalle"),
]