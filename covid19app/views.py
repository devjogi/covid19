from django.shortcuts import render
from django.views.generic import TemplateView
from . import scrap_country

def index(request):
    return render(request,'index.html')

def data(request):
    print(request.GET['contry'])
    dict = scrap_country.scrap(request.GET['contry'])
    print(dict)
    return render(request,'data.html',dict)

def symptoms(request):
    return render(request,'symptoms.html')

def precaution(request):
    return render(request,'precaution.html')