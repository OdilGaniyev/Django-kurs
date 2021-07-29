from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    name = 'Odil'
    names = ['Oybek', 'Shoxzod', 'Madinabonu']
    return render(request, 'index.html',{'ism': name , 'ismlar': names})


