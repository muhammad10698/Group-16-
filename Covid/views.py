from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from blog.models import BlogPost
from blog.views import blog_post_detail_view
from blog.models import *


from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone



def home_page(request):
    blogs = BlogPost.objects.all();

    return render(request, "home.html", {'blogs':blogs})


def about_page(request):
    return render(request, "about.html", {"title": "about"})


def contact_page(request):
    return render(request, "contact.html", {"title": "contact us"})


def instructions(request):
    return render(request, "instructions.html", {"title": "contact us"})


def adminpage(request):
    return render(request,"adminpage.html", {"title": "contact us"})


def adminprofile(request):
    return render(request,"adminprofile.html", {"title": "contact us"})


def menu(request):
    return render(request,"menu.html", {"asd":"asd"})


def HealthAndCare(request):
    blogs = BlogPost.objects.all
    
    return render(request, "HealthAndCare.html", {'blogs': blogs})


def Markets(request):
    blogs = BlogPost.objects.all();

    return render(request, "Markets.html",{'blogs':blogs})


def Restaurants(request):
    blogs = BlogPost.objects.all();
    return render(request, "Restaurants.html", {'blogs':blogs})

def UsersTable(request):
    users=user.objects.all()
    return render(request,"UsersTable.html",{'users':users})

def DeleteUsers(request):
    users=user.objects.all()
    return render(request, "DeleteUsers.html", {'users': users})

def places(request):
    blogs = BlogPost.objects.all()
    return render(request,"places.html",{'blogs':blogs})


def delete_user(request,user_id):
    users=user.objects.get(pk=user_id)
    users.delete()
    return redirect('DeleteUsers')


def ShowRestaurants(request):
    blogs = BlogPost.objects.all()
    return render(request,"ShowRestaurants.html",{'blogs': blogs})



def example_page(request):
    context       = {"title":"Example"}
    template_name = "hello_world.html"
    template_obj  = get_template(template_name)
    rendered_item = template_obj.render(template_name)
    return HttpResponse(rendered_item) #render(request,"hello_world.html",{"title": "contact us"})


