from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^profile', views.profile, name='profile'),
]
