from django import ModelForm
from cliente.models import *

class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'