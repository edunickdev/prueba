from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def gallery(request):
    imagen = {'imagen 1', 'imagen 2', 'imagen 3', 'imagen 4', 'imagen 5'}
    context = {'imagen': imagen}
    return render(request, 'gallery.html', context)


def pruebas(request):
    return render(request, 'layouts/base.html', {})
