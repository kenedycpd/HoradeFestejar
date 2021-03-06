from django.db import models


class Evento(models.Model):
	pessoas = models.IntegerField('Quantas Pessoas')
	data = models.CharField('Data Evento',max_length=50,null=True)
	hora_inicio = models.CharField('Inico Evento',max_length=50)
	hora_fim = models.CharField('Fim Evento',max_length=50)
	atividade = models.CharField('Atividades', max_length=200)
	inicio = models.CharField('Inicio',null=True,blank=True,max_length=50)
	fim = models.CharField('Fim',null=True,blank=True,max_length=50)
	nome = models.CharField('Nome do Local', max_length=150)
	endereco = models.CharField('Endereço', max_length=150)
	obs = models.CharField('Observação',max_length=200)
	cliente = models.CharField('Nome', max_length=100,null=True)
	email = models.EmailField('E-mail')
	phone = models.CharField('Telefone', max_length=15)
	cpf = models.CharField('CPF', max_length=15)
	
	class Meta:
		verbose_name_plural = 'Evento'
		verbose_name = 'Evento'
	def __str__(self):
		return self.pessoas