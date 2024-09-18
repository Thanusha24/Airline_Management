# accounts/urls.py
from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
   	path('', views.home, name='home'),
	path('home', views.home, name='home'),
	path('package1/', views.package1, name='package1'),
	path('about1/', views.about1, name='about1'),
	path('hotels1/', views.hotels1, name='hotels1'),
	path('Flights/', views.Flights, name='Flights'),
	path('gallery1/', views.gallery1, name='gallery1'),
	path('form/',views.snippet_detail,name='snippet_detail'),
	path('snippet',views.snippet_detail),
]