from django.shortcuts import render

from .models import Noticia

def index(request):
    noticias = Noticia.objects.order_by('-fecha')  # las más recientes primero
    return render(request, 'home/index.html', {'noticias': noticias})