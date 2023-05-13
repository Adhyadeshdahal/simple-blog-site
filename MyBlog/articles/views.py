from django.shortcuts import render,redirect
from articles.models import Articles
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
def articleList(request):
    article=Articles.objects.all()
    print(article[0].slug)
    return render(request,"articles/index.html",{'article':article})
def indarticle(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request,'articles/indarticle.html',{'article': article})

@login_required(login_url="../accounts/login/")
def createArticle(request):
    if request.method=="POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()

            return redirect('articles:createArticle')
        
        else :
            pass
       
    elif request.method =="GET":
        form = forms.CreateArticle()
        return render(request,"articles/create.html",{'form':form})



