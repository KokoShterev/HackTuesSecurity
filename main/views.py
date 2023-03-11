from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import CreateNewPassword, Register, TwoFactorAuthentication
from .decorations import *
from main.helper_functions.password_hash import encrypt, decrypt


# Create your views here.
@login_required(login_url="login")
def password_list(request):
    passwords = request.user.passwords_set.filter(user_id=request.user.id)
    for password in passwords:
        password.website_password = decrypt(password.website_password)
    return render(request, "main/list.html", {"passwords": passwords})


@login_required(login_url="login")
def add_password(request):
    if request.method == "POST":
        form = CreateNewPassword(request.POST)
        if form.is_valid():
            n = form.cleaned_data["website"]
            p = form.cleaned_data["website_password"]
            p = encrypt(p)
            request.user.passwords_set.create(website=n, website_password=p)
            return HttpResponseRedirect("/passwords")
        else:
            print(form.errors)
    else:
        form = CreateNewPassword()
    return render(request, "main/add_password.html", {"form": form}, {})


@login_required(login_url="login")
def home(response):
    return render(response, "main/home.html", {})


@unauthenticated_user
def register(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)

    return render(request, "main/register.html", {"form": form})


@unauthenticated_user
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                messages.info(request, "Username or password is incorrect")
        else:
            print("Error")
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})


@login_required(login_url="login")
def logout_request(request):
    logout(request)
    return redirect("home")
