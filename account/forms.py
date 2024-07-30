from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    full_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class': 'form-control'
                                                                                 , 'placeholder': 'Full Name'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"
                                                                                   , "placeholder": "Password"}))


class RegisterForm(forms.Form):
    full_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "First Name"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Password"}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "E-mail"}))



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

