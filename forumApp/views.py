from django.shortcuts import render, redirect
from forumApp.models import Articles
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages




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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid username or password')
        
    return render(request, "registration/login.html")



def logout_page(request):
    logout(request)
    return redirect('login')



def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('create_article')
            except:
                messages.error(request, 'Username already exists')
                
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'registration/register.html')



def profile_page(request):
    context = { 'username': request.user.username, }
    return render(request, 'profile.html', context)