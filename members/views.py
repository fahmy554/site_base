from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template('index.html')

    return HttpResponse(template.render())

def store(request):
    template = loader.get_template('index.html')

    return HttpResponse(template.render())
