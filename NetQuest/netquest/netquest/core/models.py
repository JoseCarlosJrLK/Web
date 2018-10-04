from django.db import models


class UserManager(models.Manager):
	"""docstring for UserManager"""
	def search(self, query):
		return self.get_queryset().filter(models.Q(email__icontains=query) | models.Q(matricula__icontains=query))
		


class User(models.Model):
	
	matricula = models.BigIntegerField('Matricula')
	nome = models.CharField('Nome', max_length=100, null=True)
	email = models.EmailField('Email', max_length=100, null=False)
	password = models.CharField('PassWord', max_length=30)

	start_date = models.DateField('Data de Inicio', null=True, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)

	objects = UserManager()

	def __str__(self):
		return self.matricula

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = "Usuarios"
		ordering = ['matricula']


class Quest(models.Model):
	
	pergunta = models.CharField('Pergunta', max_length=255, blank=False, null=True)
	quest1 = models.CharField('Questao01', max_length=255, blank=False, null=False)
	quest2 = models.CharField('Questao02', max_length=255, blank=False, null=False)
	quest3 = models.CharField('Questao03', max_length=255, blank=False, null=False)
