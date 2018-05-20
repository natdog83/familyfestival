from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from website.forms import ContactForm


def index(request):
    return render(request, 'website/home.html')


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'name', '')
            contact_email = request.POST.get(
                'email', '')
            form_content = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'website/contact.html', {
        'form': form_class,
    })
