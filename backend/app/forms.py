from django import forms
from django.contrib.auth.forms import UserCreationForm
from  .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']
    
    email = forms.Field(widget=forms.EmailInput(attrs={
        'class':"input-field",
        "placeholder":"Enter Email",
    }), label='')
    username = forms.Field(widget=forms.TextInput(attrs={
          'class':"input-field",
          "placeholder":"Enter username" 
    }), label='')
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
          'class':"input-field",
          "placeholder":"Enter password",
    }), label='')
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
          'class':"input-field",
          "placeholder":"confirm password",
          
    }), label='')
    
       
        