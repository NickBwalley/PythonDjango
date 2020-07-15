from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hi(request):
    return render(request,'Nicky/homepage.html')
def hello(request):
    return render(request,'Nicky/nicky1.css')
