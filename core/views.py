from django.shortcuts import render, redirect
from cliente.models import Evento
from .forms import EventoForm

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
