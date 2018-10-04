# -*- coding: utf-8 -*- 
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User 
from .models import Quest

class UserModelForm(forms.ModelForm):
	User._meta.get_field('email').blank = False
	class Meta:
		model = User
		fields = ('username','email','password')
		widgets ={
			'username': forms.TextInput(attrs={'class':'form-control', 'maxlength':100}),
			'email': forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
			'password': forms.PasswordInput(attrs={'class':'form-control', 'maxlength': 255,'placeholder':'*****'}),
		}

		error_messages = {
			'username':{
				'required':'Este Campo é Obrigatório'
			},
			'email':{
				'required':'Este Campo é Obrigatório'
			},
			'password':{
				'required':'Este Campo é Obrigatório'
			}
		}
	def save(self, commit=True):
		user = super(UserModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class Questionario(forms.ModelForm):

	class Meta:
		model = Quest
		fields = ('pergunta','quest1','quest2','quest3')
		widgets = {
			'pergunta': forms.TextInput(attrs={'class':'text-dark'}),
			'Chkquest1': forms.TextInput(attrs={'class':'form-check-input', 'type':'checkbox', 'name':'quest1'}),
			'quest1': forms.TextInput(attrs={'class':'text-dark form-check-label'}),
			'Chkquest2': forms.TextInput(attrs={'class':'form-check-input', 'type':'checkbox', 'name':'quest2'}),
			'quest2': forms.TextInput(attrs={'class':'text-dark form-check-label'}),
			'Chkquest3': forms.TextInput(attrs={'class':'form-check-input', 'type':'checkbox', 'name':'quest3'}),
			'quest3': forms.TextInput(attrs={'class':'text-dark form-check-label'}),
		}

class Contato(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='Email')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea)

class UserLogin(forms.Form):

	matricula = forms.CharField(label='Matricula', max_length=12)
	senha = forms.CharField(label='Senha', max_length=100)
