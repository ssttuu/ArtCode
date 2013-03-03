from ArtCode.Layout.models import Rectangle
from ArtCode.Blog.models import Post

from django.shortcuts import render_to_response
from django.views.generic import ListView




class RectangleList(ListView):
    model = Rectangle
    template_name = 'rectangle_list.html'


def home(request):
    size = (4, 3)
    rect = Rectangle.objects.random(sizeX=size[0],sizeY=size[1])
    posts = Post.objects.shuffle()
    data = {"rectangle":rect}
    data.update( rect.formatBoxes( posts))

    return render_to_response('index.html', data )

def project(request, projectSlug=None):
    post = Post.objects.filter(slug=projectSlug)
    return render_to_response('base_project.html', {"project": post })

def post(request, postSlug=None):
    if not postSlug:
        return render_to_response('base_project.html')

    return render_to_response('base_project.html', {"project":{"title": postSlug or "projects" }})

def about(request):
    return render_to_response('about.html')