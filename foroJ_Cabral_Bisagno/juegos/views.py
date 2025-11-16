from django.shortcuts import render

def juegos(request):
    return render(request, 'juegos/juegos.html')