from django.http import HttpResponse
from django.shortcuts import render,redirect



def Dashboard(request):
    return HttpResponse('<h1>HELLO PUBLIC</h1>')


