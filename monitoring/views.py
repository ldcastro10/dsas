from django.http import HttpResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to my web site")

