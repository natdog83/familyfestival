from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from website.forms import ContactForm


def index(request):
    return render(request, 'website/home.html')


def contact(request):
    return render(request, 'website/contact.html')
