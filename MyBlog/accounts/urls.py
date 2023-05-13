from django.contrib import admin
from django.urls import path,include
from accounts import views

app_name="accounts"
urlpatterns = [
    path('signup/',views.signUp,name='signUp'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logOutView,name="logout")
]