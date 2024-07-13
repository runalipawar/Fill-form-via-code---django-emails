from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
import os

def index(request):
    return render(request, 'sendemail/index.html')

def send_test_email(request):
    email = EmailMessage(
        'Python (selenium) Assignment - Runali Pawar',
        'Dear Medius Technology, \n\nSubmitting the assignment with all required documents and supporting materials attached:\n\n',
        'runalipawar72@gmail.com',
        ['tech@themedius.ai'],
    )

    file_path = os.path.join(os.path.dirname(__file__), 'attachments/screenshot.png')
    email.attach_file(file_path)

    document1_path = os.path.join(os.path.dirname(__file__), 'attachments/GoogleFormSelenium.pdf')
    email.attach_file(document1_path)

    # document2_path = os.path.join(os.path.dirname(__file__), 'attachments/document2.docx')
    # email.attach_file(document2_path)

    email.send()

    return HttpResponse('Email sent successfully with attachment!')
