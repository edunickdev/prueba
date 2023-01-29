from django.shortcuts import render
from .models import Author, Entry


# Create your views here.
def queries(request):
	# obtener todos los elementos
	authors = Author.objects.all()
	
	# obtener segun filtros particulares
	filtered = Author.objects.filter(email='brian85@example.com')
	
	# obtener un unico objeto
	unique = Author.objects.get(id=4)
	
	# obtener los 10 elementos primeros unicamente
	limitado = Author.objects.all()[:10]
	
	# obtener 10 valores, saltando los primeros 5
	offsets = Author.objects.all()[5:10]
	
	# obtener todos los elementos ordenados
	orders = Author.objects.all().order_by('email')
	
	# obtener todos los elementos cuyo id sea menor o igual a 15
	date = Author.objects.filter(id__lte=15)
	
	# obtener todos los elementos que contienen algo a buscar
	content = Author.objects.filter(name__contains='yes')
	
	return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'unique': unique, 'limitado': limitado, 'offsets': offsets, 'orders': orders, 'date': date, 'content': content})
