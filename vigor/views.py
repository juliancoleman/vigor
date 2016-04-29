from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UserCreationFormExtended
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from .models import User

def index(request):
    template = loader.get_template("vigor/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect("/vigor/dashboard") # change to just `/dashboard` when in production
        else:
            print("Internal Server Error")
    return render(request, 'vigor/login.html')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = UserCreationFormExtended(data = request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/vigor/dashboard") # change to just `/dashboard` when in production
            else:
                print("Internal Server Error")
        else:
            print(form.errors)
    else:
        form = UserCreationFormExtended()
    return render(request, 'vigor/signup.html', {'form': form})

def dashboard(request):
    return HttpResponse("Dashboard Page.")

def profile(request):
    return HttpResponse("Profile Page.")

def add_item(request):
    return HttpResponse("Should include a form with a redirect to dash on submit. The data entered should also appear on the dash")

def users(request):
    return HttpResponse(User.objects.all())
