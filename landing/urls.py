from django.conf.urls import url
from django.contrib import admin

from .views import home, about, contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
]