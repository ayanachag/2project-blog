from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная": "/", "o блоге": "/about", "страница поста": "/post"}

def main_page(request):
    # menu = {"главная": "/", "каталог": "/catalog", "о сайте": "/about"}
    # menu = ["главная", "каталог", "о сайте"]
    title = "Главная страница"
    # dict = {"name": "Ivan", "age": "20"}
    # browser = request.META.get("HTTP_USER_AGENT")
    data = {"menu": MENU, "title": title}
    return render(request,"./index.html", context=data)

def about_page(request):
    title = "О блоге"
    data = {"menu": MENU, "title": title}
    return render(request,"./about blog.html", context=data)

def post_page(request):
    title = "Страница поста"
    data = {"menu": MENU, "title": title}
    return render(request,"./post.html", context=data)