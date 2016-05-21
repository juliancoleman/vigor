from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'vigor.views.index', name='index'),
    url(r'^sign_out/$', 'vigor.ajax.sign_out', name='sign_out'),
    url(r'^signin/$', 'vigor.views.login_view', name='login'),
    url(r'^register/$', 'vigor.ajax.register', name='register'),
    url(r'^preferences/$', 'vigor.views.preferences', name='preferences'),
    url(r'^dashboard/$', 'vigor.views.dashboard', name='dashboard')
]
