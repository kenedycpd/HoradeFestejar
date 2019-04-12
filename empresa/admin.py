from django.contrib import admin
from .models import Empresa
# Register your models here.
@admin.register(Empresa)
class EmpresaForm(admin.ModelAdmin):
	list_display = ('nome','cnpj','telefone','email','endereco','numero','cidade','estado')
	search_fields = ('nome','cnpj','cidade','estado')