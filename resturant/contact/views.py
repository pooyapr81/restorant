from django.shortcuts import render
from django.views import View
from .forms import ContactForm


class ContactView(View):
    form_class = ContactForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'contact/contact.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'contact/contact.html', {'form': form})
