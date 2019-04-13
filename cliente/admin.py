from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = ('pessoas','data','hora_inicio','hora_fim','atividade','inicio','fim',
	'nome','endereco','obs','cliente','email','phone')
