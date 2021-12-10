from django.shortcuts import render, redirect

from catalogo.models import Animal, Protectora, Rescate
from catalogo.models import Protectora
from django.views import generic
from catalogo.forms import ProtectoraForm, AnimalForm, RescateForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

# Create your views here.

def indice(request):
    '''
    Página inicial de nuestra web
    '''
    datos = {'autor': 'Laura Garcia'}
    # últimos 5 rescates del catálogo
    rescates = Rescate.objects.all().order_by('-id')[:5]

    protectoras = Protectora.objects.all()
    datos['rescates'] = rescates
    datos['coordenadas'] = '41.6447628,-0.9253731'
    datos['protectoras'] = protectoras

    return render(request, 'index.html',
        context=datos)

# ----------- TODOS LOS DATOS

def todas_protectoras(request):
    protectoras = Protectora.objects.all().order_by('nombre_protectora')
    return render(request, 'todas_protectoras.html', context = {'protectoras':protectoras})

def todos_animales(request):
    animales = Animal.objects.all().order_by('nombre_raza')
    return render(request, 'todos_animales.html', context = {'animales':animales})

def todos_rescates(request):
    rescates = Rescate.objects.all().order_by('nombre_animal')
    return render(request, 'todos_rescates.html', context = {'rescates':rescates})

# ----------- CREACIONES
@login_required
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

@login_required
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

@login_required
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

# ----------- LISTVIEWS

class ProtectorasListView(generic.ListView):
    '''Vista genérica para nuestro listado de protectoras'''
    model = Protectora
    #paginate_by = 15
    queryset = Protectora.objects.all().order_by('nombre_protectora', 'ciudad')

class AnimalesListView(generic.ListView):
    '''Vista genérica para nuestro listado de animales'''
    model = Animal
    #paginate_by = 15
    queryset = Animal.objects.all().order_by('nombre_raza', 'especie')

class RescatesListView(generic.ListView):
    '''Vista genérica para nuestro listado de rescates'''
    model = Rescate
    #paginate_by = 15
    queryset = Rescate.objects.all().order_by('nombre_animal', 'especie')

# ----------- MODIFICACIONES

class ModificarProtectora(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    model = Protectora
    fields = '__all__'
    template_name = 'modificar_protectora.html'
    success_url = '/'
    success_message = "%(nombre_protectora)s se ha modificado correctamente"

class ModificarAnimal(SuccessMessageMixin, generic.UpdateView):
    model = Animal
    fields = '__all__'
    template_name = 'modificar_animal.html'
    success_url = '/'
    success_message = "%(esepecie)s, %(nombre_raza)s se ha modificado correctamente"

class ModificarRescate(SuccessMessageMixin, generic.UpdateView):
    model = Rescate
    fields = '__all__'
    template_name = 'modificar_rescate.html'
    success_url = '/'
    success_message = "%(nombre_animal)s se ha modificado correctamente"

# ----------- BUSCAR

class SearchResultsListView(generic.ListView):
    model = Rescate
    context_object_name = 'rescate_list'
    # template_name = 'rescates/search_results.html'
    def get_queryset(self): # new
        # buscar en nombre de animal y en especie
        query = self.request.GET.get('q')
        q1 = Q(nombre_animal__icontains = query)
        q2 = Q(especie__especie__icontains=query)
        return Rescate.objects.filter(q1 | q2)

# ----------- ELIMINACIONES

class EliminarProtectora(generic.DeleteView):
    model = Protectora
    #success_url = '/catalago/protectoras' #reverse('listado_protectoras')
    success_url = '/'
    success_message = "La protectora se ha borrado correctamente"
    template_name = 'protectora_confirmar_borrado.html'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarProtectora, self).delete(
            request, *args, **kwargs)

class EliminarAnimal(generic.DeleteView):
    model = Animal
    #success_url = '/catalago/animales' #reverse('listado_animales')
    success_url = '/'
    success_message = "El animal se ha borrado correctamente"
    template_name = 'animal_confirmar_borrado.html'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarAnimal, self).delete(
            request, *args, **kwargs)

class EliminarRescate(generic.DeleteView):
    model = Rescate
    #success_url = '/catalago/rescates' #reverse('listado_rescates')
    success_url = '/'
    success_message = "El rescate se ha borrado correctamente"
    template_name = 'rescate_confirmar_borrado.html'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarRescate, self).delete(
            request, *args, **kwargs)

# -----------

@login_required
def protectora_modif(request):
    '''
    Lista para modificar protectora en concreto
    '''
    lista_protectoras = Protectora.objects.all() 
    context = {'protectoras': lista_protectoras}
    return render(request, 'listar_modificar_protectora.html', context)

@login_required
def protectora_elim(request):
    '''
    Lista para eliminar protectora en concreto
    '''
    lista_protectoras = Protectora.objects.all() 
    context = {'protectoras': lista_protectoras}
    return render(request, 'listar_eliminar_protectora.html', context)

    
@login_required
def animal_modif(request):
    '''
    Lista para modificar animal en concreto
    '''
    lista_animales = Animal.objects.all() 
    context = {'animales': lista_animales}
    return render(request, 'listar_modificar_animal.html', context)

@login_required
def animal_elim(request):
    '''
    Lista para eliminar animal en concreto
    '''
    lista_animales = Animal.objects.all() 
    context = {'animales': lista_animales}
    return render(request, 'listar_eliminar_animal.html', context)

    
@login_required
def rescate_modif(request):
    '''
    Lista para modificar rescate en concreto
    '''
    lista_rescates = Rescate.objects.all() 
    context = {'rescates': lista_rescates}
    return render(request, 'listar_modificar_rescate.html', context)
    
@login_required
def rescate_elim(request):
    '''
    Lista para eliminar protectora en concreto
    '''
    lista_rescates = Rescate.objects.all() 
    context = {'rescates': lista_rescates}
    return render(request, 'listar_eliminar_rescate.html', context)

