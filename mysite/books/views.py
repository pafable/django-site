from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h>This is the books homepage</h>")
    