from django.contrib import admin
from .models import *
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'name']
admin.site.register(Book,QuestionAdmin)