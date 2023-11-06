from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl bg-teal-100 text-black',
        'autocomplete': 'off',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': 'w-full py-4 px-6 rounded-xl bg-teal-100 text-black',
        'autocomplete': 'off',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl  bg-teal-100 text-black',
        'autocomplete': 'off',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Your Password',
        'class': 'w-full py-4 px-6 rounded-xl  bg-teal-100 text-black',
        'autocomplete': 'off',
    }))



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl bg-teal-100 text-black',
        'autocomplete': 'off',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl bg-teal-100 text-black',
        'autocomplete': 'off',
    }))