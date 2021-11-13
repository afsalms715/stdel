from django.shortcuts import render, redirect
from . models import contacts,services
import smtplib
import pywhatkit
from datetime import datetime
# Create your views here.
def fun(request):
    obj=services.objects.all()

    return render(request,'index.html',{'objects':obj})

def submit(request):
    name = request.POST['name']
    emil = request.POST['email']
    phNo = request.POST['phNo']
    msg="""Subject:Details of client.....\n"""
    msg+=str(name+'\n'+emil+'\n'+phNo)
    print(msg)
    cnts=contacts(name=name,email=emil,phNo=phNo)
    cnts.save()
    sendemail(msg)
    #sendwhatsup(msg)
    return redirect(fun)

def sendemail(msg):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('blackblimmer007@gmail.com','althaf007')
    server.sendmail('blackblimmer007@gmail.com','afsalms715@gmail.com',msg)
    server.quit()

def sendwhatsup(msg):
    now = datetime.now()
    now = datetime.now()
    h =int(now.strftime("%H"))
    m =int(now.strftime("%M"))
    m+=2
    print("Current Time =",h,m)
    pywhatkit.sendwhatmsg("+919526615282",msg,h,m)
