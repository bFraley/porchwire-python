from django.http import HttpResponse, Http404
from django.shortcuts import render

# Home
def index(request):
    return render(request, 'index.html')