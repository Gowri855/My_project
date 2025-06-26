from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
   username=forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   email=forms.EmailField(max_length=254,required=True,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
   password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
   
   class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')