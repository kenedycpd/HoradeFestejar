from django.forms import ModelForm
from cliente.models import Evento
from empresa.models import Empresa

class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'

class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa
		fields = '__all__'