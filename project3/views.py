
from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    person = {'name':'Majharul','class':12,'marks':[10,12,36,24],'food':['Burger','egg','meat','milk']}
    return render(request,'home.html',person)