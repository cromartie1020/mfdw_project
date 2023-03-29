from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

def signup(request):
    subject = 'welcome to GFG world'
    message = 'Hi user, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['hrc245@gmail.com' ]
    send_mail( subject, message, email_from, recipient_list )
    
    return render(request,'contact/signup.html')
    
    