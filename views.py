from django.shortcuts import render
from django.http import HttpResponse
from website.forms import ContactForm

def index(request):
    return render(request, 'website/home.html')


def contact(request):
    form_class = ContactForm
    return render(request, 'website/contact.html', {
        'form': form_class,
    })
