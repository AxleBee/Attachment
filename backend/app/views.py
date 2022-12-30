from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import *


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{form.cleaned_data["email"]} registered successfullly')
    context = {'form': form}
    return render(request, 'app/register.html', context)


def login_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        if current_user.user_type == "supervisor":
            pass
        if current_user.user_type == "employer":
            pass
        if current_user.user_type == "student":
            pass
    email = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{user.username} logged in successfully.')
        
        else:
            messages.warning(request, 'password or email is incorrect.' )
    return render(request, 'app/login.html', context={"email": email})



    
    

def logout_view(request):
    print(request.user)
    logout(request)
    return redirect('login')
