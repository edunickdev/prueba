from django.http import HttpResponse
from .models import Comment


# Create your views here.

def test(request):
    return HttpResponse('Hola desde la app comentarios')


def create(request):
    nombres = ['Eduard', 'Sofia', 'Orlando']
    for i in nombres:
        comment = Comment(name=i, score=5, comment='Este es mi primer objeto comentarios')
        comment.save()
        
    return HttpResponse('funcion de creacion completa')
# comment = Comment.objects.create(name='Eduard')  # FORMA 2


# def delete(request):    FORMA 1
#       comment = Comment.objects.get(name='Nicolas')
#       comment.delete()'''
    
def delete(request):      # FORMA 2
    nombres = ['Eduard', 'Sofia', 'Orlando']
    for i in nombres:
        Comment.objects.filter(name=i).delete()
    return HttpResponse('funcion de borrado esta completa')
