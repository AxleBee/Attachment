from django.shortcuts import redirect, render
from django.contrib import messages
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
    context = {}
    return render(request, 'app/login.html', context)


def logout_view(request):
    return render(redirect, 'app:login')
