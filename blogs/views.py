from django.http import HttpResponse
from django.shortcuts import render_to_response
from NullSpace.blogs import *

def index(request):
    return render_to_response('index.html')
