from .views import *
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^futureweeks', futureweeks, name='futureweeks'),
]