from django.contrib import admin

from newapp.models import Client, Trainer, Login

from django.contrib.auth.models import User


# # Register your models here.
admin.site.register(Client)
admin.site.register(Trainer)
admin.site.register(Login)

