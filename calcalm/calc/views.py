from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def homepage(request):
	return render(request,"calc/home.html")
def operate(request):
	val1=int(request.GET['num1'])
	val2=int(request.GET['num2'])
	op=request.GET['o']
	if op=='+':
		ans=val1+val2		
	elif op=='-':
		ans=val1-val2
	elif op=='*':
		ans=val1*val2
	else:
		if val2==0:
			ans="Sorry"
		else:
			ans=val1/val2
	if ans==int(request.GET['num3']):
		return render(request,"calc/result.html",{'result':ans, 'flag':1, 'result1':int(request.GET['num3'])})
	else:
		return render(request,"calc/result.html",{'result':ans, 'flag':0, 'result1':int(request.GET['num3'])})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("calc:login_request")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return redirect("calc:login_request")

    form = UserCreationForm
    return render(request = request,
                  template_name = "calc/register.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Success")
                return redirect("calc:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return redirect("calc:login_request")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "calc/login.html",
                    context={"form":form})		

def logout_request(request):
	logout(request)
	return render(request,'calc/home.html')