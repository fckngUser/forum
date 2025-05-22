from django.contrib import admin
from django.urls import path

from forumApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('create/', views.create_article_page, name='create_article'),
]
