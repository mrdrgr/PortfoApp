from django.shortcuts import render
from django.contrib import messages
from .models import Message

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            Message.objects.create(email=email, subject=subject, message=message)
            messages.success(request, 'Your message was successfully sent.')
        except:
            messages.error(request, 'Your message has not been sent.')

    return render(request, 'main/contact.html')