from django.http import HttpResponseRedirect
from django.shortcuts import render

from.forms import BlogForm
from .models import Blog

def base_list(request):
    posts = Blog.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "base.html", context)

def post_list(request):
    posts = Blog.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Blog.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, "post_detail.html", context)

def post_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')
    context = {
        'form': form,
        'form_type': 'Create'
    }
    return render(request, "post_create.html", context)

def post_edit(request, post_id):
    post = Blog.objects.get(id=post_id)
    form = BlogForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')
    context = {
        'form': form,
        'form_type': 'Edit'
    }

    return render(request, "post_create.html", context)

