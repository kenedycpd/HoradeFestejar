from django.contrib import admin
from .models import *

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = ('pessoas','data','hora_inicio','hora_fim')
	search_fields = ('data_inicio',)

@admin.register(AgendaEvento)
class AgendaEventoAdmin(admin.ModelAdmin):
	list_display = ('atividade','inicio','fim')
	search_fields = ('atividade',)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
	list_display = ('nome','endereco')
	search_fields = ('nome',)

@admin.register(DadosPessoais)
class DadosPessoaisAdmin(admin.ModelAdmin):
	list_display = ('nome','email','phone')
	search_fields = ('nome','phone')