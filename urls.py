from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
]
