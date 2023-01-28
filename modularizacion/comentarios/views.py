from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse('Hola desde la app comentarios')


def create(request):
    comment = Comment(name='Nicolas', score=5, comments='Este es mi primer objeto comentarios')
    comment.save()
    return HttpResponse('Primera funcion CRUD')
