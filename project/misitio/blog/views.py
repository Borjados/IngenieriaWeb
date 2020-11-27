from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Post

def index(request):
    posts = get_list_or_404(Post.objects.order_by('titulo'))
    context = {'lista_posts' : posts}
    return render(request, 'index.html', context)
    
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post' : post}
    return render(request, 'detail.html', context)