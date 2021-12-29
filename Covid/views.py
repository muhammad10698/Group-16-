from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from blog.models import BlogPost
from blog.views import blog_post_detail_view

def home_page(request):
    blogs = BlogPost.objects.all();
    return render(request, "home.html", {'blogs':blogs})


def about_page(request):
    return render(request, "about.html", {"title": "about"})


def contact_page(request):
    return render(request, "contact.html", {"title": "contact us"})


def instructions(request):
    return render(request, "instructions.html", {"title": "instructions"})

def menu(request):
    return render(request,"menu.html", {"title":"menu"})


def HealthAndCare(request):
    blogs = BlogPost.objects.all
    
    return render(request, "HealthAndCare.html", {'blogs': blogs})


def Markets(request):
    blogs = BlogPost.objects.all();

    return render(request, "Markets.html",{'blogs':blogs})


def Restaurants(request):
    blogs = BlogPost.objects.all();
    return render(request, "Restaurants.html", {'blogs':blogs})


def example_page(request):
    context       = {"title":"Example"}
    template_name = "hello_world.html"
    template_obj  = get_template(template_name)
    rendered_item = template_obj.render(template_name)
    return HttpResponse(rendered_item) #render(request,"hello_world.html",{"title": "contact us"})


def increase(request,blogId,pop):
    originalObj = BlogPost.objects.get(id = blogId)
    if originalObj.population == originalObj.capacity :
        blogs = BlogPost.objects.all();
        return render(request,"home.html",{'blogs':blogs})
    else:    
        originalObj.population = pop + 1
        originalObj.save()
        blogs = BlogPost.objects.all();
        return render(request,"home.html",{'blogs':blogs})

def decrease(request,blogId,pop):
    originalObj = BlogPost.objects.get(id = blogId)
    if originalObj.population == 0 :
        blogs = BlogPost.objects.all();
        return render(request,"home.html",{'blogs':blogs})
    originalObj.population = pop - 1
    originalObj.save()
    blogs = BlogPost.objects.all();
    return render(request,"home.html",{'blogs':blogs})


def To_Use(request):
    return render(request,"To_Use.html", {"title":"To_Use"})

