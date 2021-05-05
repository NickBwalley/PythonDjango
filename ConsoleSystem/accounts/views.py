from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("HomePage")


def products(request):
    return HttpResponse("ProductPage")


def customer(request):
    return HttpResponse("CustomersPage")

