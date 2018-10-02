from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLogin
from .forms import UserModelForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return render(request, 'index2.html')

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect ('netquest')
	return render (request, 'login.html')


def do_logout(request):
	logout(request)
	return redirect ('home')

def contato(request):
	return render(request, 'contato.html')

@login_required
def netquest(request):
	return render(request, 'questionario.html')

def cadastro(request):
	
	form = UserModelForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('login')
	return render(request, 'cadastro.html', context)