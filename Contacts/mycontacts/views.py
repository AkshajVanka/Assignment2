from django.shortcuts import render
from django.http import HttpResponse
import operator

def mycontactdetails(requests):
    return render(requests,'mycontacts/contactdetails.html')

def home(requests):
    return HttpResponse('<h1>Home Page</h1>')
