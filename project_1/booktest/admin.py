from django.contrib import admin
from .models import HeroInfo,BookInfo

# Register your models here.

admin.site.register(BookInfo)
admin.site.register(HeroInfo)

