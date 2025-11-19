from django.urls import path
from . import views

urlpatterns = [
    path('', views.plataformas, name='plataformas'),
    path("pc/", views.pc, name="pc"),
    path("playstation/", views.playstation, name="playstation"),
    path("xbox/", views.xbox, name="xbox"),
    path("switch/", views.switch, name="switch"),
]