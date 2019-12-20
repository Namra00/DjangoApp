from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>Welcome to Django</h1>")

def v1(response):
    return HttpResponse("<h2>View 1<h2>")
