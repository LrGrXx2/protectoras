from django.forms import ModelForm
from catalogo.models import Protectora, Animal, Rescate
#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/forms


class ProtectoraForm(ModelForm):
    '''Formulario para crear protectoras'''
    class Meta:
        model = Protectora
        fields = '__all__'

class AnimalForm(ModelForm):
    '''Formulario para crear animales'''
    class Meta:
        model = Animal
        fields = '__all__'

class RescateForm(ModelForm):
    '''Formulario para crear rescates'''
    class Meta:
        model = Rescate
        fields = '__all__'