
from django.shortcuts import render

from newapp.models import Client, Trainer


def admin_home(request):
    return render(request, "admin/admin_base.html")



def admin_client_view(request):
    data=Client.objects.all()

    return render(request, "admin/admin_client_view.html", {"data":data})


def admin_trainer_view(request):
    data =Trainer.objects.all()

    return render(request, "admin/admin_trainer_view.html", {"data": data})


