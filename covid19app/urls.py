from django.urls import path
from covid19app.views import index
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index),
]