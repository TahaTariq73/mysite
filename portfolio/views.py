from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import Post, Comment
import json

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    params = {"posts": Post.objects.all()}
    return render(request, "blog.html", params)

def post(request, id):
    post = Post.objects.filter(post_id=id)[0]
    params = {
        "post": post,
        "comments": Comment.objects.filter(comment_post=post),
        "can_comment" : request.user.is_authenticated
    }
    return render(request, "post.html", params) 

def comment(request, id):
    if request.method == "POST" and request.user.is_authenticated:
        comment_content = request.POST.get("content")
        comment_user = User.objects.filter(username=request.user.username)[0]
        comment_post = Post.objects.filter(post_id=id)[0]

        comment = Comment(comment_content=comment_content, comment_user=comment_user, comment_post=comment_post)
        comment.save()
        obj = {"content": f"{comment.comment_content}", "username": f"{comment.comment_user.username}",
               "timestamp": f"{comment.timestamp}"
        }
        response = str(json.dumps(obj))
        return HttpResponse(response)

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not name.isalnum():
            return HttpResponse("Username must be alpha numeric !")
        try:
            siteUser = User.objects.create_user(name, email, password)
            siteUser.save()
            return redirect("/login")
        except Exception as err:
            return HttpResponse("Having an issue in submitting your form !")
    else:
        return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(username=name, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            return HttpResponse("Invalid credentials, Please try again")

    else:
        return render(request, "signin.html")

def logout(request):
    auth_logout(request)
    return redirect("/login/")