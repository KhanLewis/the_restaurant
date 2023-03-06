from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm
# Create your views here.


class HomepageView(generic.ListView):
    model = Booking
    template_name = "index.html"


class MakeBookingView(View):
    form = BookingForm
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(data=request.POST)
        form.owner = request.user
        if form.is_valid():
            saved_booking = form.save()
            saved_booking.owner = request.user
            saved_booking.save()
            return HttpResponseRedirect('/mybooking/')

        return render(request, self.template_name, {'form': form})


class MyBookingView(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "view_booking.html"
    def get_object_list(self, request):
        obj = Booking.object.filter(owner=request.user)
    

class MenuView(generic.ListView):

    model = Booking
    template_name = "menu.html"
