from django.conf.urls import url

from . import views

app_name = "vigor"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^users/$', views.users, name='users')
]
