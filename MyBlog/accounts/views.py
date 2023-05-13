from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def signUp(request):
   if request.method =="POST":
     form = UserCreationForm(request.POST)
     if form.is_valid():
       form.save()
       username = form.cleaned_data['username']
       password = form.cleaned_data['password1']
       user = authenticate(username=username, password=password)
       login(request,user)
       return redirect('articles:articleList')
      #log the user in
       
     else:
      return HttpResponse("")

   elif request.method == 'GET':
       form=UserCreationForm()
       return render(request,'accounts/signUp.html',{'form': form})

   
def loginView(request):
  if request.method == "GET":
    form= AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
  elif request.method=="POST":
    form=AuthenticationForm(data=request.POST)
    if form.is_valid():
      #login
      user=form.get_user()
      login(request,user)
      return redirect('articles:articleList')

def logOutView(request):
  if request.method == "POST":
    logout(request)
    return redirect('articles:articleList')

  
  

   

