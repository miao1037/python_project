from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^addbookhandler/$',views.addbookhandler,name='addbookhandler'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^delete/(\d+)/$',views.delete,name='delete'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addherohandler/$',views.addherohandler,name='addherohandler')
]