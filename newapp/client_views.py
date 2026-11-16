from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PaymentForm, ClientForm
from .models import Schedule, Client, Booking, DietPlan
from django.shortcuts import render


@login_required(login_url='login_view')
def client_home(request):
    data = Schedule.objects.all()
    return render(request, "client/client_base.html", {"data": data})


@login_required(login_url='login_view')
def join_schedule(request, id):

    schedule =Schedule.objects.get(id=id)
    data= request.user

    client_data = Client.objects.get(client=data)

    print(client_data)
    booking = Booking.objects.create(client=client_data, schedule=schedule)

    return redirect('client_home')


@login_required(login_url='login_view')
def booking_page(request):
    user = request.user
    print(user.id)

    client_data= Client.objects.get(client=user)
    print(client_data.id)

    bookings = Booking.objects.filter(client=client_data)

    return render(request, 'client/booking_page.html', {'bookings': bookings})



@login_required(login_url='login_view')
def payment(request, id):
    booking = Booking.objects.get(id=id)
    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            payment_data = form.save(commit=False)
            payment_data.booking = booking
            payment_data.save()
            booking.status = 3
            booking.save()

            return redirect('booking_page')

    return render(request, 'client/payment.html', {'form': form})



@login_required(login_url='login_view')
def client_profile(request):
    data = Client.objects.get(client=request.user)
    return render(request, 'client/client_profile.html', {'data': data})



@login_required(login_url='login_view')
def client_profile_update(request, id):
    data = Client.objects.get(id=id)
    form = ClientForm(instance=data)

    if request.method == "POST":
        form = ClientForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return redirect("client_profile")

    return render(request,"client/client_profile_update.html",{"form": form})


@login_required(login_url='login_view')
def view_diet_plan(request):
    client = Client.objects.get(client=request.user)
    data = DietPlan.objects.filter(client=client).first()

    return render(request, 'client/view_diet.html', {'data': data})
