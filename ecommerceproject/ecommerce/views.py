from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models  import Language
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
	lang=Language.objects.all()
	return render(request,'ecommerce/home.html',{'lang':lang})
def content(request, pk):
	lang=Language.objects.get(id=pk)
	if request.user.is_authenticated:
		return render(request,'ecommerce/content.html', {'lang':lang})
	else:
		return redirect('login_request')	

def register(request):
	form=CreateUserForm()
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('home')
	context={'form':form}
	return render(request,'ecommerce/register.html',context)
def login_request(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			lang=Language.objects.all()
			context={'lang':lang, 'user':user}
			login(request,user)
			return render(request,'ecommerce/home.html',context)
		else:
			messages.info(request,'username aor password not correct')

	return render(request,'ecommerce/login.html')

def logout_request(request):
	logout(request)
	return redirect('home')

