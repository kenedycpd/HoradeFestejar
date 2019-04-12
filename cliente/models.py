from django.db import models


class Evento(models.Model):
	pessoas = models.IntegerField('Quantas Pessoas')
	data = models.DateField('Data Evento')
	hora_inicio = models.TimeField('Inico Evento')
	hora_fim = models.TimeField('Fim Evento')
	class Meta:
		verbose_name_plural = 'Evento'
		verbose_name = 'Evento'
	def __str__(self):
		return self.pessoas

class AgendaEvento(models.Model):
	atividade = models.CharField('Atividades', max_length=200)
	inicio = models.DateField('Inicio',null=True,blank=True)
	fim = models.DateField('Fim',null=True,blank=True)

	class Meta:
		verbose_name_plural = 'Agenda do Evento'
		verbose_name = 'Agenda do Evento'
	def __str__(self):
		return self.atividade

class Local(models.Model):
	nome = models.CharField('Nome do Local', max_length=150)
	endereco = models.CharField('Endereço', max_length=150)
	obs = models.TextField('Observação')

	class Meta:
		verbose_name_plural = 'Local'
		verbose_name = 'Local'
	def __str__(self):
		return self.nome

class DadosPessoais(models.Model):
	nome = models.CharField('Nome', max_length=100)
	email = models.EmailField('E-mail')
	phone = models.CharField('Telefone', max_length=11)

	class Meta:
		verbose_name_plural = 'Dados Pessoais'
		verbose_name = 'Dados Pessoais'
	def __str__(self):
		return self.nome