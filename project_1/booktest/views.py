from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader,RequestContext

# Create your views here.


def index(requset):
    # print("请求",requset)
    # return HttpResponse("首页")

    #加载模板
    # indextem = loader.get_template('booktest/index.html')
    # #构造上下文
    # cont = {"username":"miao"}
    # #渲染模板
    # result = indextem.render(cont)
    # return HttpResponse(result)

    cont = {"username":"miao"}
    return render(requset,'booktest/index.html',cont)

def list(requset):
    # return HttpResponse("列表页")

    # listtem = loader.get_template('booktest/list.html')
    # booklist = BookInfo.objects.all()
    # cont = {"booklist":booklist}
    # result = listtem.render(cont)
    # return HttpResponse(result)
    booklist = BookInfo.objects.all()
    cont = {"booklist": booklist}
    return render(requset,'booktest/list.html',cont)


def detail(requset,id):
    # try:
    #     book = BookInfo.objects.get(pk = int(id))
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse("请输入正确id")

    # try:
    #     detailtem = loader.get_template('booktest/detail.html')
    #     book = BookInfo.object.get(pk = int(id))
    #     cont = {"book":book}
    #     result = detailtem.render(cont)
    #     return HttpResponse(result)
    # except:
    #     return HttpResponse("请输入正确id")

    book = BookInfo.objects.get(pk=id)
    cont = {"book":book}
    return render(requset,'booktest/detail.html',cont)
