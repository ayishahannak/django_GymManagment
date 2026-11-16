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
   path("logout",views.logout_view,name="logout"),
   path("admin_client_view",admin_views.admin_client_view,name="admin_client_view"),
   path("admin_trainer_view",admin_views.admin_trainer_view,name="admin_trainer_view"),


   path("trainer_delete/<int:id>/",admin_views.trainer_delete,name="trainer_delete"),
   path("client_delete/<int:id>/",admin_views.client_delete,name="client_delete"),
   path("trainer_update/<int:id>/",admin_views.trainer_update,name="trainer_update"),
   path('client_block/<int:id>/', admin_views.client_block, name='client_block'),
   path('client_unblock/<int:id>/', admin_views.client_unblock, name='client_unblock'),
   path('client_restore/<int:id>/', admin_views.client_restore, name='client_restore'),
   path('deleted_clients', admin_views.deleted_clients, name='deleted_clients'),

   path("time_schedule",admin_views.time_schedule,name="time_schedule"),
   # path("time_schedule_view",admin_views.time_schedule_view,name="time_schedule_view"),
   path("schedule_update/<int:id>/", admin_views.schedule_update, name="schedule_update"),
   path("time_view",admin_views.time_view,name="time_view"),

   path("join_gym/<int:id>/", client_views.join_schedule, name="join_gym"),
   path("booking_page",client_views.booking_page,name="booking_page"),
   path('booking_page_admin', admin_views.booking_page_admin, name='booking_page_admin'),


   path('approve_booking/<int:id>/', admin_views.approve_booking, name='approve_booking'),
   path('reject_booking/<int:id>/', admin_views.reject_booking, name='reject_booking'),

   path('payment/<int:id>/',client_views.payment, name='payment'),
   path('paid_clients',admin_views.paid_clients,name='paid_clients'),


   path('trainer_profile', trainer_views.trainer_profile, name='trainer_profile'),
   path("trainer_profile_update/<int:id>/", trainer_views.trainer_profile_update, name="trainer_profile_update"),


   path('client_profile', client_views.client_profile, name='client_profile'),
   path("client_profile_update/<int:id>/", client_views.client_profile_update, name="client_profile_update"),
   path('add_diet_plan/', trainer_views.add_diet_plan, name='add_diet_plan'),
   path('trainer_diet_plans/', trainer_views.trainer_diet_plans, name='trainer_diet_plans'),
   path('view_diet_plan/', client_views.view_diet_plan, name='view_diet_plan'),
]


























