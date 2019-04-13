from django.db import models


class Evento(models.Model):
	pessoas = models.IntegerField('Quantas Pessoas')
	data = models.DateField('Data Evento')
	hora_inicio = models.TimeField('Inico Evento')
	hora_fim = models.TimeField('Fim Evento')
	atividade = models.CharField('Atividades', max_length=200)
	inicio = models.DateField('Inicio',null=True,blank=True)
	fim = models.DateField('Fim',null=True,blank=True)
	nome = models.CharField('Nome do Local', max_length=150)
	endereco = models.CharField('Endereço', max_length=150)
	obs = models.TextField('Observação')
	cliente = models.CharField('Nome', max_length=100,null=True)
	email = models.EmailField('E-mail')
	phone = models.CharField('Telefone', max_length=11)

	class Meta:
		verbose_name_plural = 'Evento'
		verbose_name = 'Evento'
	def __str__(self):
		return self.pessoas