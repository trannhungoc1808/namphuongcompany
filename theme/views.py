from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.template.response import TemplateResponse

# Create your views here.
def homepage(request):
    return TemplateResponse(request, 'base.html')

def contact(request):
    #check for POST requests on load.
    request.method == 'POST'
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    email = request.POST.get('email')

    if subject and message and email:
        try:
            send_mail(subject, message, email, ['lamanhnguyen135@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Thanks for your email')

    else:
        #loading contacts.html if no requests
        #return render(request, '/theme/templates/base.html')
        return HttpResponse('nope')
