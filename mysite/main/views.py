from django.shortcuts import render
from django.http import httpResponse
# Create your views here.

def index(response):
    return httpResponse("<h1>Welcome to Django</h1>")

def v1(response):
    return httpResponse("<h2>View 1<h2>")
