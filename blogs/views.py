from django.shortcuts import render
from.models import BlogPost


def home(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request,'blogs/home.html', context=context)