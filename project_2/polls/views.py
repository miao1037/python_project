from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Options
from django.template import loader
# Create your views here.

def index(request):
    # return HttpResponse("首页")
    # cont = {"username":"miao"}
    return render(request,'polls/index.html',{"username":"POLL"})

def list(request):
    queslist = Questions.objects.all()
    cont = {"queslist":queslist}
    return render(request,'polls/list.html',cont)
#
#
def detail(request,id):
    ques = Questions.objects.get(pk=id)
    cont = {"ques":ques}
    return render(request,'polls/detail.html',cont)

def poll(request,cid,qid):
    choose = Options.objects.get(pk=cid)
    choose.ovote +=1
    choose.save()
    ques = Questions.objects.get(pk=qid)
    cont = {"ques": ques}
    return render(request, 'polls/detail.html', cont)

