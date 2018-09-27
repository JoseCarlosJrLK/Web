from django import forms

class Contato(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='Email')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea)


class UserCadastro(forms.Form):

	matricula = forms.CharField(label='Matricula', max_length=12)
	nome = forms.CharField(label="Nome", max_length=100)
	email = forms.EmailField(label='Email')
	senha = forms.CharField(label='Senha', max_length=100)

class UserLogin(forms.Form):

	matricula = forms.CharField(label='Matricula', max_length=12)
	senha = forms.CharField(label='Senha', max_length=100)