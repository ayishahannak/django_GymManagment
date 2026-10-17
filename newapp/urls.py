from django.urls import path

from newapp import views, admin_views, trainer_views, client_views

urlpatterns = [
   # path("",views.home,name="home"),
   path("",views.index,name="index"),
   path("dashboard",views.dashboard,name="dashboard"),

   path("user_add",views.user_add,name="user_add"),
   path("trainer_add", views.trainer_add, name="trainer_add"),

   path("admin_home/",admin_views.admin_home,name="admin_home"),
   path("trainer_home/",trainer_views.trainer_home,name="trainer_home"),
   path("client_home/",client_views.client_home,name="client_home"),

   path("login_view",views.login_view,name="login_view"),
   path("admin_client_view",admin_views.admin_client_view,name="admin_client_view"),
path("admin_trainer_view",admin_views.admin_trainer_view,name="admin_trainer_view"),
]