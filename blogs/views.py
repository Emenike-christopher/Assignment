from django.shortcuts import render, get_object_or_404
from.models import BlogPost
from .forms import BlogForm
from django.shortcuts import redirect

def home(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request,'blogs/home.html', context=context)

def blog_detail(request, blog_id):
    blog = get_object_or_404 (BlogPost, id=blog_id)
    #blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, template_name = 'blogs/blog_detail.html', context=context)

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user.username
            new_blog.save()
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
        context = {'form': form}
    return render(request, template_name='blogs/create_blog.html', context=context)

def update_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(data=request.POST, instance=blog)
        if form.is_valid():
            edited_blog = form.save(commit=False)
            if not edited_blog.author:
                edited_blog.author = request.user
            edited_blog.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
        context = {'form': form, 'blog': blog}
        return render(request,'blogs/update_blog.html', context=context)
    
def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    else:
     context = {'blog': blog}
    return render(request, 'blogs/delete_blog.html', context=context)