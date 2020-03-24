from django.contrib import admin
from django.urls import include,path
from covid19app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('covid19app.urls')),
]
