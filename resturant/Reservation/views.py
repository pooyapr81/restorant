from django.shortcuts import render
from django.views import View
from .forms import ReservationForm


class ReservView(View):
    form_class = ReservationForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'reservation/reservation.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'reservation/reservation.html', {'form': form})
