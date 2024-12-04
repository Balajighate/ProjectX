from django.shortcuts import render,redirect

from .forms import CreateUserForm,LoginForm,CreateRecordForm,UpdateRecordForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

from .models import Employee

from django.contrib import messages

from django.core.mail import send_mail 

# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    form = CreateUserForm()

    if request.method=="POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,"Account Created Successfully")

            return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context)


def my_login(request):
    form = LoginForm()

    if request.method=="POST":
        form = LoginForm(request,data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)

                messages.success(request,"Sign Suceessful")

                return redirect('dashboard')
    context={'form':form}
    return render(request,'login.html',context)


def logout(request):
    auth.logout(request)

    return redirect('login')


def dashboard(request):
    emp = Employee.objects.all()

    send_mail('Welcome To Crm ', 'Thank you for visiting our site', 'balajighate25@gmail.com', ['balajighate25@gmail.com','pratiksutar03@gmail.com','mansisonawane58@gmail.com'], fail_silently=False)



    context = {'emp':emp}
    return render(request,'dashboard.html',context)

def createrecord(request):
    form = CreateRecordForm()

    if request.method=="POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
        
    context = {'form':form}
    return render(request,'createrecord.html',context)

def updaterecord(request,pk):
    emp = Employee.objects.get(id=pk)

    form = UpdateRecordForm(instance=emp)

    if request.method=="POST":
        form = UpdateRecordForm(request.POST,instance=emp)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    context = {'form':form}
    return render(request,'updaterecord.html',context)    
    
def viewrecord(request,pk):
    emp = Employee.objects.get(id=pk)

    context = {'emp':emp}

    return render(request,'view_record.html',context)


def deleterecord(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()

    return redirect('dashboard')

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('login')