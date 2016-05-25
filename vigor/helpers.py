from django.http import HttpResponse

def redirect_if_authenticated(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/vigor/dashboard")
