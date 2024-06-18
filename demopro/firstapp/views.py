from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Contact
from firstapp.models import Signupdata

# Create your views here.

#database creation
def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        date=request.POST.get('dob')
        databas=Signupdata(name=name,email=email,gender=gender,date=date)
        databas.save()
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('Password')
        # Here Contact is table name 
        data=Contact(name=name,email=email,password=password)
        data.save()

    return render(request,'login.html')
    
#after creation of login() then import the => from firstapp.models import Contact


def  fun(request):
    return HttpResponse("Hello this is django")
def fun2(request):
    return HttpResponse("This is response from fun2 function")
def fun3(request):
    return render(request,'home.html')
#username->sankar12
#password->sankar1234
