from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login (AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class Trainer(models.Model):
    trainer = models.OneToOneField(Login,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
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
    is_deleted = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    membership = models.CharField(max_length=20)
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    fee = models.IntegerField()

def __str__(self):
    return f"{self.start_time} - {self.end_time}"


class Booking(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)



class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    exp_date = models.DateField()

class DietPlan(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    breakfast = models.TextField()
    lunch = models.TextField()
    snacks = models.TextField()
    dinner = models.TextField()

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title