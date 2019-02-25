from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import Booktest, Hero

# Create your views here.

def template_render(template_path, request, context_dict = {}):
    #1、装载模板文件
    #2、定义模板上下文
    #3、产生html内容
    #4、返回给浏览器
    booklist = Booktest.objects.get(id=1)
    temp = loader.get_template(template_path)
    context = {'booklist':booklist}
    res_html = temp.render(context)
    return HttpResponse(res_html)


def index(request):
    return template_render("booktest/index.html", request)
    #return HttpResponse("hello World!")

def books(request):
    booklists = Booktest.objects.all()
    temp = loader.get_template("booktest/books.html")
    context = {'booklists' : booklists}
    res_html = temp.render(context)
    return HttpResponse(res_html)

def heros_in_book(request, bid):
    booklist = Booktest.objects.get(id=bid)
    heros = booklist.hero_set.all()
    temp = loader.get_template("booktest/detail.html")
    context = {'booklist':booklist, 'heros' : heros}
    res_html = temp.render(context)
    return HttpResponse(res_html)