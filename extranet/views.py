from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    XD = '123'
    return render(request, 'index.html', {'XD':XD})
