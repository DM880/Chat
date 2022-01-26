from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import generic as generic_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def sign(request):
    return render(request, "sign.html")


def sign_in(request):
    pass


def sign_out(request):
    pass
