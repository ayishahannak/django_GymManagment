
from django import forms
from django.contrib.auth.forms import UserCreationForm

from newapp import models
from newapp.models import Client, Trainer, Login,Schedule


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
        exclude = ['trainer','is_deleted','is_blocked']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields='__all__'
        exclude = ['client','is_deleted','is_blocked']

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ScheduleForm(forms.ModelForm):
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)


    class Meta:
        model = Schedule
        fields='__all__'
