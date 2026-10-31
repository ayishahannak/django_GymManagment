from django.shortcuts import render, redirect

from .models import Schedule, Client, Booking
from django.shortcuts import render

def client_home(request):
    data = Schedule.objects.all()
    return render(request, "client/client_base.html", {"data": data})



def join_schedule(request, id):

    schedule =Schedule.objects.get(id=id)
    data= request.user

    client_data = Client.objects.get(client=data)

    print(client_data)
    booking = Booking.objects.create(client=client_data, schedule=schedule)

    return redirect('client_home')



def booking_page(request):
    user = request.user
    print(user.id)

    client_data= Client.objects.get(client=user)
    print(client_data.id)

    bookings = Booking.objects.filter(client=client_data)

    return render(request, 'client/booking_page.html', {'bookings': bookings})
