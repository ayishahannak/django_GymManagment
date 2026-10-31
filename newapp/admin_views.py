from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from newapp.forms import TrainerForm, LoginForm, ScheduleForm
from newapp.models import Client, Trainer, Schedule, Booking


def admin_home(request):
    return render(request, "admin/admin_base.html")



def admin_client_view(request):
    # data=Client.objects.all()
    data = Client.objects.filter(is_deleted=False)

    return render(request, "admin/admin_client_view.html", {"data":data})


def admin_trainer_view(request):
    # data =Trainer.objects.all()
    data = Trainer.objects.filter(is_deleted=False)

    return render(request, "admin/admin_trainer_view.html", {"data": data})




def client_block(request, id):
    data = get_object_or_404(Client, id=id)
    data.is_blocked = True
    data.save()

    messages.success(request, "Client blocked successfully.")
    return redirect("admin_client_view")


def client_unblock(request, id):
    data = get_object_or_404(Client, id=id)
    data.is_blocked = False
    data.save()

    messages.success(request, "Client unblocked successfully.")
    return redirect("admin_client_view")


def trainer_block(request, id):
    data = get_object_or_404(Trainer, id=id)
    data.is_blocked = True
    data.save()

    messages.success(request, "Trainer blocked successfully.")
    return redirect("admin_trainer_view")


def trainer_unblock(request, id):
    data = get_object_or_404(Trainer, id=id)
    data.is_blocked = False
    data.save()

    messages.success(request, "Trainer unblocked successfully.")
    return redirect("admin_trainer_view")


def client_restore(request, id):
    data = Client.objects.get(id=id)
    data.is_deleted = False
    data.save()
    return redirect('admin_client_view')

def deleted_clients(request):
    data = Client.objects.filter(is_deleted=True)
    return render(request, 'admin/deleted_client.html', {'data': data})

# def trainer_delete(request,id):
#     data = Trainer.objects.get(id=id)
#     data.delete()
#
#     return redirect("admin_trainer_view")
#
#
# def client_delete(request,id):
#     data = Client.objects.get(id=id)
#
#     data.delete()
#     return redirect("admin_client_view")

def trainer_delete(request, id):
    data = Trainer.objects.get(id=id)
    data.is_deleted = True

    data.save()

    return redirect("admin_trainer_view")


def client_delete(request, id):
    data = Client.objects.get(id=id)
    data.is_deleted = True

    data.save()

    return redirect("admin_client_view")


def trainer_update(request, id):
    data = Trainer.objects.get(id=id)
    user = data.trainer

    form1 = LoginForm(instance=user)
    form2 = TrainerForm(instance=data)

    if request.method == "POST":
        form1 = LoginForm(request.POST, instance=user)
        form2 = TrainerForm(request.POST, request.FILES, instance=data)

        if form1.is_valid() and form2.is_valid():
            user_data = form1.save(commit=False)
            user_data.is_trainer = True
            user_data.save()

            trainer_data = form2.save(commit=False)
            trainer_data.trainer = user_data
            trainer_data.save()

            return redirect("admin_trainer_view")
        

    return render(request, "admin/trainer_update.html",{"form1": form1, "form2": form2})



def time_schedule(request):
    form=ScheduleForm()

    if request.method=="POST":
        form_data=ScheduleForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("time_schedule_view")
    return render(request,"admin/time_schedule.html",{"form":form})



def time_schedule_view(request):
    data=Schedule.objects.all()
    return render(request, "admin/time_schedule_view.html", {"data":data})




def schedule_update(request,id):
    data = Schedule.objects.get(id=id)
    form = ScheduleForm(instance=data)

    if request.method=="POST":
        form_data=ScheduleForm(request.POST,instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect("time_schedule_view")



    return render(request,"admin/schedule_update.html",{"data":form})



def booking_page_admin(request):
    bookings = Booking.objects.all()
    return render(request, "admin/time_schedule_view.html", {"bookings": bookings})



def approve_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.status = 1
    booking.save()

    return redirect("booking_page_admin")


def reject_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.status = 2
    booking.save()

    return redirect("booking_page_admin")