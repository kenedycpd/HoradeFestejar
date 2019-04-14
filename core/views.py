from django.shortcuts import render, redirect
from cliente.models import Evento
from empresa.models import Empresa
from .forms import EventoForm, EmpresaForm

def home(request):
	return render(request, 'index.html')

def evento(request):
	if request.method == 'POST':
		form = EventoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = EventoForm()
	return render(request, 'core/eventoform.html',{'form':form})


def servico(request):
	if request.method == 'POST':
		form = EmpresaForm(request.POSt)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = EmpresaForm()
	return render(request, 'core/empresaform.html',{'form':form})