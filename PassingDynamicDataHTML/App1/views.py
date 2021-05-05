from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home1.html', {'Name': 'NickBwalley'} )


def result(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    result = val1 + val2

    return render(request, 'results.html', {'Result':result})
    