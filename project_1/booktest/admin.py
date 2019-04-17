from django.contrib import admin
from .models import HeroInfo,BookInfo

# Register your models here.
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["Btitle"]
    list_filter = ["Btitle"]
    search_fields = ["Btitle"]
    list_per_page = 4
    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name","sex","skill"]
    list_filter = ["hname"]
    search_fields = ["hname","hcontent"]
    list_per_page = 4






admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

