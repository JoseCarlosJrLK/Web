from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCadastro
from .forms import UserLogin

# Create your views here.
def home(request):
	return render(request, 'index2.html')

def login(request):
	
	template_name = 'login.html'
	context ={}

	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():
			context['is_valid']=True
	else:
		form = UserLogin()

	context['form'] = form

	return render(request, template_name, context)

def contato(request):
	return render(request, 'contato.html')

def netquest(request):
	return render(request, 'questionario.html')

def cadastro(request):
	
	template_name = 'cadastro.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		   form.save()
		return redirect ('login.html')

	else:

		form = UserCreationForm()
	context ={
		'form':form
	}

	return render(request, template_name,context)