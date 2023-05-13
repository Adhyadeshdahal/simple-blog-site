from django.contrib import admin
from django.urls import path,include
from articles import views

urlpatterns = [
    path('index/',views.articleList,name='articleList'),
    path("<slug:slug>/",views.indarticle,name='each-article'),
    path("createArticle",views.createArticle,name="createArticle")
]