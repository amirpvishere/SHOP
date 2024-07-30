from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from account.forms import LoginForm, RegisterForm
from account.models import Account


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Account.objects.get(full_name=form.cleaned_data['full_name'])
            login(request, user)
            redirect('accounts:login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = Account.objects.create(email=form.cleaned_data['email'],
                                          password=form.cleaned_data['password'],
                                          full_name=form.cleaned_data['full_name'],
                                          image=form.cleaned_data['image'])
            login(request, user)
            return redirect('home:home')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {"form": form})


def log_out(request):
    logout(request)
    return redirect('home:home')
