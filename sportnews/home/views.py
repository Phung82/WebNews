from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,"pages/home.html")

def v_contact(request):
    return render(request,"pages/contact.html")

def v_about(request):
    return render(request,"pages/about.html")

def v_post(request):
    return render(request,"pages/post.html")


