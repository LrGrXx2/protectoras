from django.shortcuts import render, redirect

from catalogo.models import Animal, Protectora, Rescate
from catalogo.models import Protectora
from django.views import generic
from catalogo.forms import ProtectoraForm, AnimalForm, RescateForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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


def todas_protectoras(request):
    protectoras = Protectora.objects.all().order_by('nombre_protectora')
    return render(request, 'todas_protectoras.html', context = {'protectoras':protectoras})

def todos_animales(request):
    animales = Animal.objects.all().order_by('nombre_raza')
    return render(request, 'todos_animales.html', context = {'animales':animales})

def todos_rescates(request):
    rescates = Rescate.objects.all().order_by('nombre_animal')
    return render(request, 'todos_rescates.html', context = {'rescates':rescates})

# -----------

def crear_protectora(request):
    if request.method == 'POST':
        form = ProtectoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Protectora creada correctamente')
            return redirect('/')
    else:
        form = ProtectoraForm()
    datos = {'form': ProtectoraForm()}
    return render(request, 'crear_protectora.html', 
        context=datos)

def crear_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Animal creado correctamente')
            return redirect('/')
    else:
        form = AnimalForm()
    datos = {'form': AnimalForm()}
    return render(request, 'crear_animal.html', 
        context=datos)

def crear_rescate(request):
    if request.method == 'POST':
        form = RescateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Rescate creado correctamente')
            return redirect('/')
    else:
        form = RescateForm()
    datos = {'form': RescateForm()}
    return render(request, 'crear_rescate.html', 
        context=datos)

# -----------

class ProtectorasListView(generic.ListView):
    '''Vista genérica para nuestro listado de protectoras'''
    model = Protectora
    paginate_by = 15

class AnimalesListView(generic.ListView):
    '''Vista genérica para nuestro listado de animales'''
    model = Animal
    paginate_by = 15

class RescatesListView(generic.ListView):
    '''Vista genérica para nuestro listado de rescates'''
    model = Rescate
    paginate_by = 15

# -----------


class SearchResultsListView(generic.ListView):
    model = Rescate
    context_object_name = 'rescate_list'
    template_name = 'rescates/search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Rescate.objects.filter(title__icontains = query)