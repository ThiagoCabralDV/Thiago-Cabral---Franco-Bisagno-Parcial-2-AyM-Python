from django.shortcuts import render

def plataformas(request):
    return render(request, 'plataformas/plataformas.html')

def pc(request):
    return render(request, "plataformas/pc.html")

def playstation(request):
    return render(request, "plataformas/playstation.html")

def xbox(request):
    return render(request, "plataformas/xbox.html")

def switch(request):
    return render(request, "plataformas/switch.html")