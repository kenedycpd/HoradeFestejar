from django.db import models


class Empresa(models.Model):
	nome = models.CharField('Nome da Empresa', max_length=100)
	cnpj = models.CharField('CNPJ', max_length=100)
	telefone = models.CharField('Telefone', max_length=10)
	email = models.EmailField('E-mail')
	endereco = models.CharField('Endereço', max_length=100)
	numero = models.CharField('Numero', max_length=4)
	cidade = models.CharField('Cidade', max_length=100)
	est = (
		('AL', 'Alagoas'),
		('AM', 'Amapá'),
		('AM', 'Amazoanas'),
		('BA', 'Bahia'),
		('CE', 'Ceará'),
		('DF', 'Distrito Federal'),
		('ES', 'Espirito Santo'),
		('GO', 'Goiás'),
		('MA', 'Maranhão'),
		('MT', 'Mato Grosso'),
		('MS', 'Mato Grosso do Sul'),
		('MG', 'Minas Gerais'),
		('PA', 'Pará'),
		('PB', 'Paraíba'),
		('PR', 'Paraná'),
		('PE', 'Pernambuco'),
		('Pi', 'Piauí'),
		('RJ', 'Rio de Janeiro'),
		('RN', 'Rio Grande do Norte'),
		('RS', 'Rio Grande do Sul'),
		('RO', 'Rondônia'),
		('RR', 'Roraima'),
		('SC', 'Santa Catarina'),
		('SP', 'São Paulo'),
		('SE', 'Sergipe'),
		('TO', 'Tocantins'),
		)
	estado = models.CharField('Estado', max_length=2, choices=est)
	class Meta:
		verbose_name_plural = 'Empresa'
		verbose_name = 'Empresa'
	def __str__(self):
		return self.nome