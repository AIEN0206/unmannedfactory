from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Employees
import json

# Create your views here.
def index(request):
    pageTitle = "UnmannedFactory首頁"
    return render(request, "lumino/index.html", locals())
def charts(request):
    pageTitle = "#"
    return render(request, "lumino/charts.html", locals())
def elements(request):
    pageTitle = "#"
    return render(request, "lumino/elements.html", locals())
def panels(request):
    pageTitle = "#"
    return render(request, "lumino/panels.html", locals())
def widgets(request):
    pageTitle = "#"
    return render(request, "lumino/widgets.html", locals())
def login(request):
    pageTitle = "#"
    return render(request, "lumino/login.html", locals())

def getjson(request):
    pageTitle = "#"
    data = serializers.serialize("json", Employees.objects.all())
    data2= json.loads(data)
    return JsonResponse(data2, safe=False)
