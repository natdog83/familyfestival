from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('^$', views.index, name='home'),
    path(r'^contact/$', views.contact, name='contact'),
]
