from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo
from django.template import loader

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

def delete(requset,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        booklist = BookInfo.objects.all()
        cont = {"booklist": booklist}
        # return render(requset, 'booktest/list.html', cont)
        #重定向 重新向服务器发起请求 刷新url
        return HttpResponseRedirect('/booktest/list/',cont)
    except:
        return HttpResponse('删除失败')

def addhero(requset,bookid):
    return render(requset,'booktest/addhero.html',{"bookid":bookid})

def addherohandler(request):
    bookid = request.POST["bookid"]
    hname = request.POST["heroname"]
    hgender = request.POST['sex']
    hcontent = request.POST['herocontent']

    book = BookInfo.objects.get(pk=bookid)
    hero = HeroInfo()
    hero.hname = hname
    hero.hgender = True
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/',{"book":book})

