from django.urls import path
from catalogo.views import EliminarAnimal, EliminarProtectora, EliminarRescate, ProtectorasListView, RescatesListView, SearchResultsListView, \
    crear_animal, crear_protectora, crear_rescate, \
    todas_protectoras, todos_animales, todos_rescates, \
    ModificarProtectora, ModificarAnimal, ModificarRescate

urlpatterns = [
    path('protectoras/', ProtectorasListView.as_view(), name='listado_protectoras'),
    path('animales/', todos_animales, name='listado_animales'),
    path('rescates/', todos_rescates, name='listado_rescates'),

    path('buscarescates/', SearchResultsListView.as_view(), name='buscarescates'),
    
    path('protectora/crear', crear_protectora, name='crear_protectora'),
    path('animal/crear', crear_animal, name='crear_animal'),
    path('rescate/crear', crear_rescate, name='crear_rescate'),

    path('protectora/modificar/<int:pk>', ModificarProtectora.as_view(), name='modificar_protectora'),
    path('animal/modificar/<int:pk>', ModificarAnimal.as_view(), name='modificar_animal'),
    path('rescate/modificar/<int:pk>', ModificarRescate.as_view(), name='modificar_rescate'),

    path('protectora/eliminar/<int:pk>', EliminarProtectora.as_view(), name='eliminar_protectora'),
    path('animal/eliminar/<int:pk>', EliminarAnimal.as_view(), name='eliminar_animal'),
    path('rescate/eliminar/<int:pk>', EliminarRescate.as_view(), name='eliminar_rescate'),
]
