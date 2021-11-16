from django.urls import path
from catalogo.views import RescatesListView, SearchResultsListView, crear_animal, crear_protectora, crear_rescate
from catalogo.views import todas_protectoras, todos_animales, todos_rescates

urlpatterns = [
    path('protectoras/', todas_protectoras, name='listado_protectoras'),
    path('animales/', todos_animales, name='listado_animales'),
    path('rescates/', todos_rescates, name='listado_rescates'),
    path('buscarescates/', SearchResultsListView.as_view(), name='buscarescates'),
    path('protectora/crear', crear_protectora, name='crear_protectora'),
    path('animal/crear', crear_animal, name='crear_animal'),
    path('rescate/crear', crear_rescate, name='crear_rescate'),
]
