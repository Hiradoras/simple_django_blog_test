from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post

def post_pic(request):
    obj = Post.objects.all()
    context = {
        "obj" : obj
    }
    return render(request,"posts/index.html", context)
