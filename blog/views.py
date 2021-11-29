from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost






def blog_post_detail_page(request, slug):
    print("django says", request.method, request.path, request.user)
    queryset = BlogPost.objects.get(slug=slug)
    if queryset.count() >= 1:
        raise Http404
        obj = queryset.first()
  #  obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)












def blog_post_list_view(request):
    #list out objects
    #could be search
    template_name = 'Blog_Post_list.html'
    context = {'object_list': []}
    return render(request, template_name, context)



def blog_post_creat_view(request):
    # creating objects using forms
    template_name = 'Blog_post_creat.html'
    context = {'form': None}
    return render(request, template_name, context)



def blog_post_retrieve_view(request):
    return


def blog_post_update_view(request):
    return



def blog_post_delete_view(request):
    return
