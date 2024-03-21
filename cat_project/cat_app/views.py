from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Home View'
                        '<br>'
                        '<a href="/cat_app/cats/">Cats</a>')

def cats(request):
    return  HttpResponse('here is the list of cats'
                         '<br>'
                         '<a href="/cat_app/">Home</a>')