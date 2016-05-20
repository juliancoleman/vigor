import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from .forms import MealForm, UserPrefsForm, ProfileForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse
from .models import Meal, SystemMessage

def index(req):
    return render(req, 'index.html')

@csrf_exempt
def login_view(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        next = req.POST.get('next', None)
        user = authenticate(username = username, password = password)

        if user is not None:
            if user.is_active:
                login(req, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponseForbidden('This account has been disabled')
        else:
            return render(req, 'signin.html', {'next': next, 'register': settings.REGISTER, 'error': True})

    if req.method == 'GET':
        if req.user.is_authenticated():
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            next = req.GET.get('next', None)
            print(next)
            return render(req, 'signin.html', {'next': next, 'register': settings.REGISTER, 'error': False})

@login_required
@csrf_exempt
def preferences(req):
    user = req.user
    saved = False
    pw_changed = False
    password_error = None
    form = None

    if req.method == 'GET':
        form = UserPrefsForm(instance = user.prefs)
    elif req.method == 'POST':
        password = req.POST.get('password', None)
        password2 = req.POST.get('password2', None)

        if password and password2 and password != '':
            if password == password2:
                user.set_password(password)
                user.save()
                pw_changed = True
            else:
                password_error = 'The passwords you entered do not match'
        elif password and not password2:
            password_error = 'You need to confirm you password'
        elif password2 and not password:
            password_error = 'Please enter both passwords'
        form = UserPrefsForm(req.POST, instance = user.prefs)
        gender = req.POST['gender']
        birth_year = req.POST['birth_year']
        birth_month = req.POST['birth_month']
        birth_day = req.POST['birth_day']
        height_feet = req.POST['height_feet']
        height_inches = req.POST['height_inches']
        weight = req.POST['weight']
        ethnicity = req.POST['ethnicity']
        determination = req.POST['determination']

        saved_gender = str(user.prefs.gender)
        saved_birth_year = str(user.prefs.birth_year)
        saved_birth_month = str(user.prefs.birth_month)
        saved_birth_day = str(user.prefs.birth_day)
        saved_height_feet = str(user.prefs.height_feet)
        saved_height_inches = str(user.prefs.height_inches)
        saved_weight = str(user.prefs.weight)
        saved_ethnicity = str(user.prefs.ethnicity)
        saved_determination = str(user.prefs.determination)

        if gender == saved_gender and \
            birth_year == saved_birth_year and \
            birth_month == saved_birth_month and \
            birth_day == saved_birth_day and \
            height_feet == saved_height_feet and \
            height_inches == saved_height_inches and \
            weight == saved_weight and \
            ethnicity == saved_ethnicity and \
            determination == saved_determination:
            pass
        else:
            if form.is_valid():
                form.full_clean()
                form.save()
                saved = True

    return render(req, 'prefs.html', {'form': form, 'saved': saved, 'pw_changed': pw_changed, 'password_error': password_error})

def dashboard(req):
    user = req.user
    first_time = False

    if req.GET.get('first', None):
        first_time = True

    sys_messages = SystemMessage.objects.all()
    return render(req, 'dashboard.html', {'sys_messages': sys_messages, 'first_time': first_time})
