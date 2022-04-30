from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as logins
from django.contrib.auth import logout as logouts
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def Register(request):
	if request.method == "POST":
		Register_form = UserCreationForm(request.POST)
		if Register_form.is_valid():
			user = Register_form.save()
			logins(request, user)
			return redirect('home')
	else:
		Register_form = UserCreationForm()
	return render(request, 'Account/Register.html', {'Register_form': Register_form})

def login(request):
	if request.method == "POST":
		Login_form = AuthenticationForm(data=request.POST)
		if Login_form.is_valid():
			user = Login_form.get_user()
			logins(request, user)
			return redirect('home')
	else:
		Login_form = AuthenticationForm()
	return render(request, 'Account/login.html', {'Login_form':Login_form})

def logout(request):
	logouts(request)
	return redirect('MainHome')

def change_password(request):
	user = request.user.username
	if request.method == 'POST':
		pswd_change_form = PasswordChangeForm(request.user, request.POST)
		if pswd_change_form.is_valid():
			user = pswd_change_form.save()
			update_session_auth_hash(request, user)
			return redirect('MainHome')
	else:
			pswd_change_form = PasswordChangeForm(user=request.user)
			return render(request, 'Account/change_password.html', {'form': pswd_change_form, 'user': user})

