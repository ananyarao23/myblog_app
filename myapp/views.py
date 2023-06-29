from django.shortcuts import render, redirect
from datetime import datetime
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import *



def index(request):
    if request.user.is_authenticated:
        context = {
        'blogs' : BlogModel.objects.all(),
        'categories_list' : BlogModel.objects.values_list('category', flat=True).distinct()
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')
    
def explore(request):
    return render(request, 'explore.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        concern = request.POST.get('concern')
        contact = Contact(name=name, email=email, phone=phone, concern=concern,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
def register(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
    return render(request, 'register.html')
def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=uname, password = pswd)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        title = request.POST.get('title')
        category = request.POST.get('category')
        if form.is_valid():
            content = form.cleaned_data['content']
            blog = BlogModel(
                user = User.objects.get(pk=request.user.id),
                title=title,
                content=content,
                category=category,
                pub_date=datetime.today()
            )
            blog.save()
            context = {
                'form': BlogForm(),
                'error': "Articled added successfully!"
            }
            return render(request, 'add_blog.html', context)
        else:
            context = {
                'form': form,
                'error': "Form is not valid"
            }
            return render(request, 'add_blog.html', context)
    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'add_blog.html', context)
def my_account(request):
    context = {
    'blogs' : BlogModel.objects.filter(user = request.user)
    }
    return render(request, 'myaccount.html', context)
def read(request, slug):
    blog = BlogModel.objects.filter(slug = slug).first()
    context = {
        'blog' : blog
    }
    return render(request, 'read.html', context)
def delete(request, slug):
    blog_obj = BlogModel.objects.get(slug = slug)
    blog_obj.delete()
    
    context = {
    'blogs' : BlogModel.objects.filter(user = request.user )
    }
    return render(request, 'myaccount.html', context)
def update(request, slug):
    if request.method == "POST":
        form = BlogForm(request.POST)
        title = request.POST.get('title')
        category = request.POST.get('category')
        if form.is_valid():
            content = form.cleaned_data['content']
            blog = BlogModel(
                user = User.objects.get(pk=request.user.id),
                title=title,
                content=content,
                category=category,
                pub_date=datetime.today()
            )
            blog.save()
            context = {
                'blogs' : BlogModel.objects.filter(user = request.user)
            }
            return render(request, 'myaccount.html', context)
    blog_obj = BlogModel.objects.get(slug = slug)
    initial_dict = {
        'content' : blog_obj.content,
        'title' : blog_obj.title,
        'category' : blog_obj.category
    }
    form = BlogForm(initial = initial_dict)
    context = {
        'form' : form,
    }
    return(request, 'update_blog.html', context)