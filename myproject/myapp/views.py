from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import feature
from .forms import createpollform 
from .forms import createfeedback
from .models import Poll
from .models import Feedback

from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    features=feature.objects.all()
    return render(request,'poll/index.html',{'features':features})

def register(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
    
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password is not same')
            return redirect('register')
    else:
        return render(request,'poll/register.html')
def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
    
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect ('login')
    else:
        return render(request,'poll/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request,'poll/profile.html')

def contact(request):
    if request.method=='POST':
        form1=createfeedback(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
    else:
        form1=createfeedback
    context={'form':form1}
    return render(request,'poll/contact.html',context)

def list(request):
    return render(request,'poll/list.html')

def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request,'poll/home.html',context)

def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def create(request):
    
    if request.method=='POST':
        form=createpollform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=createpollform
    context={'form':form}
    return render(request,'poll/create.html',context)

def vote(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    
    if request.method=='POST':
        selected_option=request.POST['poll']
        if selected_option=='option1':
            poll.option_one_count +=1
        elif selected_option =='option2':
             poll.option_two_count +=1
        elif selected_option =='option3':
             poll.option_three_count +=1
        elif selected_option =='option4':
             poll.option_four_count +=1
        else:
            return HttpResponse(400,'Invalid Response')
        
        poll.save()
        
        return redirect('home')
        
    context={'poll':poll}
    return render(request,'poll/vote.html',context)
@user_passes_test(check_admin)
def results(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context={'poll':poll}
    return render(request,'poll/results.html',context)
    

   