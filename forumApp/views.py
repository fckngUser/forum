from django.shortcuts import render, redirect
from forumApp.models import Articles

def main_page(request):
    articles = Articles.objects.all().order_by('-id')  
    return render(request, 'main_page.html', {'articles': articles})

def create_article_page(request):
    if request.method == "POST":
        name = request.POST.get("name")  
        content = request.POST.get("content")  
        
        if name and content:  
            Articles.objects.create(name=name, content=content)
            return redirect("/")
    
    return render(request, 'create_article.html')

def login_page(request):
    context = {}
    return render(request, "registration/login.html", context)