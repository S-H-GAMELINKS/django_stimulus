from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<div controller=sample><div data-target="sample.hello"></div></div><script src="../assets/index.js"></script>')