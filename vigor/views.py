from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Vigor index.")

def login(request):
    return HttpResponse("Login Page.")

def signup(request):
    return HttpResponse("Signup Page.")

def dashboard(request):
    return HttpResponse("Dashboard Page.")

def profile(request):
    return HttpResponse("Profile Page.")
