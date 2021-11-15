from django.shortcuts import render

from catalogo.models import Rescate

# Create your views here.

def indice(request):
    '''
    Página inicial de nuestra web
    '''
    datos = {'autor': 'Laura Garcia'}
    # últimos 5 rescates del catálogo
    rescates = Rescate.objects.all().order_by('-id')[:5]

    datos['libros'] = rescates

    return render(request, 'index.html',
        context=datos)