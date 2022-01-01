from django.shortcuts import render, redirect
from qrcode import *
#for authenticates
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

from home import models

# Create your views here.
data = None


def home(request):
    # can pass variables to html page
    # context = {
    #     'name':'mohamed',
    #     'learning': 'web'
    # }
    # return HttpResponse("this is my homepage (/)")
    return render(request, 'home.html')


def material(request):
    return render(request, 'material.html')


def contact(request):
    if request.method == 'POST':
        # do stuff
        print("Got Post Request")
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = models.Contact(name=name, email=email, message=message)
        ins.save()  # save to db
        print("data has been saved")
    return render(request, 'contact.html')


# make a about page
def about(request):
    return render(request, 'about.html')


def userprofile(request):
    return render(request, 'UserProfile.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def quiz(request):
    return render(request, 'quiz.html')



def qrcode(request):
    global data
    if request.method == "POST":
        data = request.POST['data']
        img = make(data)
        img.save("static/image/test.png")
    else:
        pass
    return render(request, "qrcode.html", {'data': data})
