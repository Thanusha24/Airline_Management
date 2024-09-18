# accounts/views.py
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SnippetForm
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
  
def home(request):
		return render(request,'home.html',{})
def package1(request):
		return render(request,'package1.html',{})
def about1(request):
		return render(request,'about1.html',{})
def Flights(request):
		return render(request,'Flights.html',{})
def gallery1(request):
		return render(request,'gallery1.html',{})
def hotels1(request):
		return render(request,'hotels1.html',{})
def snippet_detail(request):
	if request.method=='POST':
		form=SnippetForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()
			return redirect('home')

	form=SnippetForm()
	return render(request,'snippet_detail.html',{'form':form})