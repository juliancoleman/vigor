from django.http import HttpResponse

def is_authenticated(request):
    return HttpResponseRedirect("/vigor/dashboard") if request.user.is_authenticated()
end
