from django.urls import path
from covid19app.views import index,data,symptoms,precaution
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index),
    url(r'^data/$',data),
    url(r'^symptoms/$',symptoms),
    url(r'^precaution/$',precaution),
]