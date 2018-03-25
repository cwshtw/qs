from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Book
from django.shortcuts import render
from django.core.cache import cache
def index(request):
    return HttpResponse("index")
def detail(request,id):
    books = Book.objects.get(pk=id)
    request.session['qs']=id
    cache.set('q1',"hhh")
    cache.get('q1')
    return render(request,"index.html",{"books":books,'id':cache.get('q1')})
# Create your views here.
