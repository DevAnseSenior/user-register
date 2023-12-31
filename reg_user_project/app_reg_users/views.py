from django.shortcuts import render
from .models import User
from django.contrib import messages


def home(request):
    users = {
        'users': User.objects.all()
    }
    return render(request, 'users/home.html', users)


def create_user(request):
    if request.method == 'POST':
        new_user = User()
        new_user.name = request.POST.get('name')
        new_user.age = request.POST.get('age')

        if not User.objects.filter(name=new_user.name):
            new_user.save()
            messages.success(request, f"User registered successfully!")
        else:
            messages.error(request, f"Error, user already registered", "danger")


    return render(request, 'users/create_user.html')
