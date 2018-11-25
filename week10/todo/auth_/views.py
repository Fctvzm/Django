from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def register(request):
	form = UserCreationForm(data=request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('main:index')
	return render(request, 'auth_/register.html', {'form': form})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('main:index')
		else:
			error = 'Your username or password is not correct'
			return render(request, 'auth_/login.html', {'error': error})
	else:
		return render(request, 'auth_/login.html')

def logout(request):
	auth.logout(request)
	return redirect('main:index')
