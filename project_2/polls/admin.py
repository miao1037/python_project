from django.contrib import admin
from .models import Questions,Options
# Register your models here.

class OptionsInline(admin.StackedInline):
    model = Options
    extra = 1

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question']
    search_fields = ['question']
    list_per_page = 4
    inlines = [OptionsInline]

class OptionsAdmin(admin.ModelAdmin):
    list_display = ['option','poll']
    list_per_page = 4





admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Options,OptionsAdmin)
