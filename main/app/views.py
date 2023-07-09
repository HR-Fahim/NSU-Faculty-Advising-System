from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests

'''
def manifest_json(request):
    file_path = settings.STATICFILES_DIRS + '/manifest.json'
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
    return response

def logo_png(request):
    file_path = settings.STATICFILES_DIRS + '/logo192.png'
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='image/png')
    return response

'''

def index(request):
    return render(request, 'index.html')

