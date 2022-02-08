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
        pass
        # return redirect("page")

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                # return redirect("page")
        else:
            return render(request, "sign.html", {"error": True})
    else:
        return render(request, "sign.html")




def sign_up(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = requst.POST.get('password2')


        if User.objects.filter(username=username).exists():
            error = f"{username} - Username already exist"
            return render(request, 'sign.html', error)

        elif User.objects.filter(email=email).exists():
            error = f"{email} - Email already exist"
            return render(request, 'sign.html', error)

        elif password1 != password2:
            error = "Passwords don't match"
            return render(request, 'sign.html', error)

        user_data = {
            'username':username,
            'email': email,
            'password': password,
            }

        User.object.create(**user_data)

        return redirect('sign')

    pass
