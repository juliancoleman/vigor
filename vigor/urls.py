from django.conf.urls import url

from . import views
from . import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_out/$', ajax.sign_out, name='sign_out'),
    url(r'^signin/$', views.login_view, name='login'),
    url(r'^register/$', ajax.register, name='register'),
    url(r'^preferences/$', views.preferences, name='preferences'),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
]
