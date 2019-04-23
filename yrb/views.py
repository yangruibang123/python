from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    return render(request,'yrb/a.html',locals())

def my_douban(request):
    data=models.douban.objects.all()
    return render(request,'yrb/b.html',locals())

def my_jindong(request):
    data=models.jingdon.objects.all()
    return render(request,'yrb/c.html',locals())