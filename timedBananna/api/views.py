from django.shortcuts import render

from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("Hello, world. You're at the API index.")

def jobs(request):
    return HttpResponse("Jobs Data below")