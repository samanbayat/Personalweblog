from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    # return HttpResponse('Hi There. About Page')
    return render(request, 'About.html')


def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'Home.html')
