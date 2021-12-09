import debug_toolbar
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from catalogo.views import EliminarAnimal, EliminarProtectora, EliminarRescate, ProtectorasListView, RescatesListView, SearchResultsListView, \
    AnimalesListView,crear_animal, crear_protectora, crear_rescate, \
    todas_protectoras, todos_animales, todos_rescates, \
    ModificarProtectora, ModificarAnimal, ModificarRescate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),
    #listar
    path('protectoras/', ProtectorasListView.as_view(), name='listado_protectoras'),
    path('animales/', AnimalesListView.as_view(), name='listado_animales'),
    path('rescates/', RescatesListView.as_view(), name='listado_rescates'),
    #buscar
    path('buscarescates/', SearchResultsListView.as_view(), name='buscarescates'),
    #crear
    path('protectora/crear', crear_protectora, name='crear_protectora'),
    path('animal/crear', crear_animal, name='crear_animal'),
    path('rescate/crear', crear_rescate, name='crear_rescate'),
    #modificar
    path('protectora/modificar/<int:pk>', ModificarProtectora.as_view(), name='modificar_protectora'),
    path('animal/modificar/<int:pk>', ModificarAnimal.as_view(), name='modificar_animal'),
    path('rescate/modificar/<int:pk>', ModificarRescate.as_view(), name='modificar_rescate'),
    #eliminar
    path('protectora/eliminar/<int:pk>', EliminarProtectora.as_view(), name='eliminar_protectora'),
    path('animal/eliminar/<int:pk>', EliminarAnimal.as_view(), name='eliminar_animal'),
    path('rescate/eliminar/<int:pk>', EliminarRescate.as_view(), name='eliminar_rescate'),
]
