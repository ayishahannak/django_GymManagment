from django.urls import path

from newapp import views

urlpatterns = [
   path("",views.home,name="home"),
   path("index",views.index,name="index"),
   path("dashboard",views.dashboard,name="dashboard"),
   path("login",views.login,name="login"),
]