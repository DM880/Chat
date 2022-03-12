from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User


from chat_app.data.chat.models import Room, Message


from chat_app.domain.chat.tasks import time_check


def sign(request):
    if request.user.is_authenticated:
        return redirect("create_room_chat")
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
            message = "Login details invalid"
            return render(request, "sign.html", {"message": message})
    else:
        return render(request, "sign.html")


def sign_up(request):

    if request.method == "POST":

        message = ""

        username = request.POST.get("username_signup")
        email = request.POST.get("email_signup")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            message = f"{username} - Username already exist"
            return render(request, "sign.html", {"message": message})

        elif User.objects.filter(email=email).exists():
            message = f"{email} - Email already exist"
            return render(request, "sign.html", {"message": message})

        elif password1 != password2:
            message = "Passwords don't match"
            return render(request, "sign.html", {"message": message})

        user_data = {
            "username": username,
            "email": email,
            "password": password1,
        }

        user = User.objects.create_user(**user_data)

        success = "Account created successfully"

        return render(request, "sign.html", {"message": message, "success":success})

    else:
        return redirect("sign")


def reset_password(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            message = 'username or email invalid'
            return render(request, 'reset_password.html', {"message":message})

        if password1 != password2:
            message = "Passwords don't match"
            return render(request, 'reset_password.html', {"message": message})

        user.set_password(password1)
        user.save()

        return redirect('sign')

    return render(request, 'reset_password.html',)


@login_required
def sign_out(request):
    logout(request)
    return redirect("sign")


# Chat Room


@login_required
def create_room_chat(request):

    if request.method == "POST":
        room_name = request.POST.get("room_name").lower()

        # if empty redirect to same page
        if not room_name:
            return redirect(request.META.get("HTTP_REFERER", "sign"))

        if Room.objects.filter(name=room_name).exists() == False:
            Room.objects.create(name=room_name)

            # add step to check if room has been called from a redirect
            request.session[f"pp_create_room_chat_{room_name}"] = True
            return redirect("choose_create_chat", room_name)

        else:
            room = Room.objects.get(name=room_name)
            # check how how much time has passed since last message
            check = time_check(room)

            # create new room if time passed is more than 10days
            if check == True:
                Room.objects.create(name=room_name)

                request.session[f"pp_create_room_chat_{room_name}"] = True
                return redirect("choose_create_chat", room_name)

            if room.private == False:
                request.session[f"chat_access_{room_name}"] = True
                return redirect("room", room_name)

            else:
                request.session[f"enter_key_access_{room_name}"] = True
                return redirect("enter_key", room_name)

    return render(request, "create_room_chat.html")


@login_required
def choose_create_chat(request, room_name):

    # check if room has been called from create_room_chat
    if f"pp_create_room_chat_{room_name}" in request.session:

        if request.method == "POST":

            is_private = request.POST.get('private')
            key = request.POST.get('key')

            if is_private == 'Public':
                request.session[f"chat_access_{room_name}"] = True
                return redirect('room', room_name)

            else:
                room = Room.objects.get(name=room_name)
                room.private = True
                room.key = key
                room.save()

                request.session[f"chat_access_{room_name}"] = True

                return redirect('room', room_name)

        return render(request, "choose_create_chat.html", {'room_name':room_name})


@login_required
def enter_key(request, room_name):

    if f"enter_key_access_{room_name}" in request.session:

        if request.method == "POST":

            check_key = request.POST.get('check_key')

            room = Room.objects.get(name=room_name)

            if check_key == room.key:
                request.session[f"chat_access_{room_name}"] = True
                return redirect('room', room_name)

            else:
                render(request,'enter_key.html', {'room_name':room_name})

        return render(request,'enter_key.html', {'room_name':room_name})


@login_required
def room(request, room_name):

    if f"chat_access_{room_name}" in request.session:

        room_messages = Room.objects.get(name=room_name)
        all_messages = Message.objects.filter(room=room_messages)

        return render(
            request,
            "chat_room.html",
            {
                "room_name": room_name,
                "all_messages": all_messages,
            },
        )
