from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from newapp.forms import LoginForm, ClientForm, TrainerForm




# Create your views here.
# def home(request):
#     return HttpResponse("welcome to gym management")

def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")


# def loginpage(request):
#     return render(request, "login.html")


def user_add(request):
    form1=LoginForm()
    form2=ClientForm()

    if request.method=="POST":
        form1=LoginForm(request.POST)
        form2=ClientForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user_data=form1.save(commit=False)
            user_data.is_client=True
            user_data.save()

            user1 = form2.save(commit=False)
            user1.client=user_data
            user1.save()

            return redirect("index")

    return render(request, "user_add.html",{"form1":form1,"form2":form2})



def trainer_add(request):
    form1=LoginForm()
    form2=TrainerForm()

    if request.method=="POST":
        form1=LoginForm(request.POST)
        form2=TrainerForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            user_data=form1.save(commit=False)
            user_data.is_trainer=True
            user_data.save()

            user1 = form2.save(commit=False)
            user1.trainer=user_data
            user1.save()

            return redirect("index")

    return render(request, "trainer_add.html",{"form1":form1,"form2":form2})





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_home/')

            elif user.is_client:
                return redirect('client_home/')

            elif user.is_trainer:
                return redirect('trainer_home/')

        else:
            print('invalid')

    return render(request, "login.html")





