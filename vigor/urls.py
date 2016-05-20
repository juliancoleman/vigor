from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'vigor.views.index', name='index'),
    url(r'^sign_out/$', 'vigor.ajax.sign_out', name='sign_out'),
    url(r'^signin/$', 'vigor.views.login_view', name='login'),
    url(r'^register/$', 'vigor.ajax.register', name='register'),
    url(r'^preferencess/$', 'vigor.views.preferences', name='preferences'),
    url(r'^dashboard/$', 'vigor.views.dashboard', name='dashboard')
    # url(r'^auth/$', views.signin, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # url(r'^profile/$', views.profile, name='profile'),
    # url(r'^add_item/$', views.add_item, name='add_item'),
    # url(r'^users/$', views.users, name='users')
]
