# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2020-03-26 06:45
# @Last Modified by:   Admin
# @Last Modified time: 2020-03-26 09:45
from django.shortcuts import render
from django.views.generic import TemplateView
from . import scrap_country


def index(request):
    return render(request, 'index.html')


def data(request):
    print(request.GET['contry'])
    s = (request.GET['contry']).lower()
    print(s)
    dict = scrap_country.scrap((request.GET['contry']).lower())
    print(dict)
    # str = '123'
    return render(request, 'data.html', {'dict': dict})


def symptoms(request):
    return render(request, 'symptoms.html')


def precaution(request):
    return render(request, 'precaution.html')
