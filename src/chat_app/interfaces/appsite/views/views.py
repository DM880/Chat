from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import generic as generic_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User


def sign(request):
    return render(request, "sign.html")


def sign_in(request):

    if request.user.is_authenticated:
        return redirect("create_room_chat")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect("create_room_chat")
        else:
            error = "Login details invalid"
            return render(request, "sign.html", {"error": error})
    else:
        return render(request, "sign.html")


def sign_up(request):

    if request.method == "POST":

        username = request.POST.get("username_signup")
        email = request.POST.get("email_signup")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            message = f"{username} - Username already exist"
            return render(request, "sign.html", {'message':message})

        elif User.objects.filter(email=email).exists():
            message = f"{email} - Email already exist"
            return render(request, "sign.html", {'message':message})

        elif password1 != password2:
            message = "Passwords don't match"
            return render(request, "sign.html", {'message':message})

        user_data = {
            "username": username,
            "email": email,
            "password": password1,
        }

        User.objects.create(**user_data)

        message = "Account created successfully"

        return render(request, "sign.html", {'message':message})

    else:
        return redirect("sign")


# Chat Room

@login_required
def create_room_chat(request):
    return render(request, 'create_room_chat.html')


@login_required
def room(request, room_name):
    return render(request, 'chat_room.html', {'room_name':room_name})