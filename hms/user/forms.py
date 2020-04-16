from django import forms
# from django.contrib.auth import login, authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewGuestRegister(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class GuestLoginForm():
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
    