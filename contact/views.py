from django.shortcuts import redirect, render
from .models import Info
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        return redirect(reverse ('jobs:available_jobs'))

    return render(request,'contact/contact.html',{'myinfo':myinfo})