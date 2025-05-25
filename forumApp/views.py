from django.shortcuts import render, redirect, get_object_or_404
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
            Articles.objects.create(name=name, content=content, author=request.user)
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
    if not request.user.is_authenticated:
        return redirect('login')  
    
    user_articles = Articles.objects.filter(author=request.user).order_by('-id')
    
    context = {
        'user': request.user,
        'user_articles': user_articles,
    }
    return render(request, 'profile.html', context)



def article_delete(request, article_id):
    if request.method == 'POST':
        try:
            article = Articles.objects.get(id=article_id, author=request.user)
            article.delete()
        except Articles.DoesNotExist:
            pass  
    return redirect('profile')



def article_edit(request, article_id):
    article = get_object_or_404(Articles, id=article_id, author=request.user)  
    
    if request.method == 'POST':
        article.name = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('profile')
    
    return render(request, 'edit_article.html', {'article': article})