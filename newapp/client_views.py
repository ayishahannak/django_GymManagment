from django.shortcuts import render


def client_home(request):
    return render(request, "client/client_base.html")