from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login (AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class Trainer(models.Model):
    trainer = models.OneToOneField(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    weight = models.IntegerField()
    height = models.IntegerField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Client(models.Model):
    client = models.OneToOneField(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    membership = models.CharField(max_length=20)
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name




