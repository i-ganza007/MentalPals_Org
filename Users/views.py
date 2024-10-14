from os import name
from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return HttpResponse('<h1>Register Page Now!!</h1>')



def profile(request):
    return HttpResponse('<h1>Profile Page Now!!</h1>')