import json
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import SystemMessage, UserPrefs

def response_mimetype(req):
    if "application/json" in req.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

class JSONResponse(HttpResponse):
    """JSON response class."""

    def __init__(self, obj=None, json_opts=None, mimetype="application/json", *args, **kwargs):
        if obj is None:
            obj = {}
        if json_opts is None:
            json_opts = {}
        content = json.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)

def sign_out(req):
    logout(req)
    return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def register(req):
    if settings.REGISTER:
        if req.method == "POST":
            username = req.POST['username']
            password = req.POST['password']
            email = req.POST['email']

            user = User.objects.create_user(username, email, password)
            UserPrefs.objects.create(user = user)
            user2 = authenticate(username = username, password = password)
            login(req, user2)
            return HttpResponseRedirect(reverse('preferences'))
    else:
        return HttpResponseForbidden('Registration is disabled')

def read_sys_message(request, msg_id):
    user = request.user
    try:
        msg = SystemMessage.objects.get(pk=msg_id)
    except SystemMessage.DoesNotExist:
        return HttpResponse(status=404)

    msg.users_read.add(user)
    return HttpResponse(status=206)
