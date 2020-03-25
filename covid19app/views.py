from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request,'index.html')

def data(request):
    print(request.GET['contry'])
    return render(request,'data.html')
