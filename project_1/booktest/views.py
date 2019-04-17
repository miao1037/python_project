from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(requset):
    print("请求",requset)
    return HttpResponse("首页")
