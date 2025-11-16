from django.shortcuts import render

def plataformas(request):
    return render(request, 'plataformas/plataformas.html')