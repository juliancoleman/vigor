from django.http import HttpResponse

def is_authenticated(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/vigor/dashboard")
