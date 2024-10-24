from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'dashboard/index.html')

def staff(request):
    return render(request,'dashboard/staff.html')


def customer(request):
    return render(request,'dashboard/customer.html')

def book(request):
    return render(request,'dashboard/book.html')



