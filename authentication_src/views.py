from django.shortcuts import render, redirect, get_object_or_404
from authentication_src.forms import Signup_form, Login_form, Updater_form
from authentication_src.models import SchoolManagerModel
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def inscription_form(request):
    form = Signup_form()
    message = ''
    if request.method == "POST":
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
            message = 'user created succefully !'
        else:
            message = 'verifier vos données'
    return render(request, 'authentication_src/inscription.html', context={'message':message, 'form':form})


def login_user(request):
    form = Login_form()
    message = ''
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'verifier vos données'
    return render(request, 'authentication_src/login.html', context={'message':message, 'form':form})

@login_required
def home(request):
    message = 'welcome to ur home !'
    return render(request, 'authentication_src/home.html', {'message':message})

def logout_user(request):
    logout(request)
    return redirect('login-user')


@login_required
def get_users(request):
    users = SchoolManagerModel.objects.all()
    return render(request, 'authentication_src/get_users.html', {'users':users})


@login_required
def update_user(request, id):
    user = get_object_or_404(SchoolManagerModel, id=id)
    form = Updater_form(instance=user)
    message = ''
    if request.method == "POST":
        form = Updater_form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            message = 'user updated'
        else:
            message = 'verify data !'
    return render(request, 'authentication_src/user_modify.html', context={'message':message, 'form':form})

@login_required
def delete_user(request, id):
    user = get_object_or_404(SchoolManagerModel, id=id)
    user.delete() 
    ADMIN = 'admin'
    return redirect('get-users')


