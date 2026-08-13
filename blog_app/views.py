from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog_app.models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponseRedirect("/")


from django.contrib.auth.decorators import login_required


@login_required
def draft_list(request):
    post = Post.objects.filter(published_date__isnull=True)
    return render(
        request,
        "draft_list.html",
        {"posts": post},
    )


@login_required
def draft_detail(request, pk):
    post = Post.objects.get(pk=pk, published_date__isnull=True)
    return render(
        request,
        "draft_detail.html",
        {"post": post},
    )
