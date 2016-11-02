from django.shortcuts import render
from register.forms import UploadFileForm
from register.models import UploadFile
from django.contrib import messages
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import email
import fileCompare
import pySendEmail

# Create your views here.
#each view exists as a function, 

#inside your app folder, create urls.py to map this view and url

def register_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['docfile'])
            
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)            

    form = UploadFileForm() # A empty, unbound form
    return render(request, 'register/register.html', {'form': form})

    # Handle file upload

    # Render list page with the documents and the form
def handle_uploaded_file(f):
    with open('/var/www/djDailyReport/src/src.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    fileCompare.fileCompare('/var/www/djDailyReport/src/src.txt', '/var/www/djDailyReport/src/result.csv', '/var/www/djDailyReport/src/result-all.csv')
    
    receipients= ['nzhang@futuredial.com']
    receipients= ['lynnwang@futuredial.com', 'nzhang@futuredial.com']
    
    pySendEmail.sendEmail(receipients,'/var/www/djDailyReport/src/result.csv', '/var/www/djDailyReport/src/result-all.csv')
    return