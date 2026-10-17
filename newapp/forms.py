
from django import forms
from django.contrib.auth.forms import UserCreationForm

from newapp.models import Client, Trainer, Login


class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields=['username','password1','password2']


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields='__all__'
        exclude = ['trainer']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields='__all__'
        exclude = ['client']


