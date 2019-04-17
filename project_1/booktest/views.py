from django.shortcuts import render
from django.http import HttpResponse
from  .models import BookInfo


# Create your views here.


def index(requset):
    print("请求",requset)
    return HttpResponse("首页")

def list(requset):
    return HttpResponse("列表页")

def detail(requset,id):
    try:
        book = BookInfo.objects.get(pk = int(id))
        return HttpResponse(book)
    except:
        print("请输入正确id")
