from django.conf.urls import url
from . import data

urlpatterns = [
    url(r'^$/', data.index, name='index'),
]
