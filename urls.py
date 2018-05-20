from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    url('^', views.index, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
]
