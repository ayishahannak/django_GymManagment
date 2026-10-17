from django.shortcuts import render


def trainer_home(request):
    return render(request, "trainer/trainer_base.html")