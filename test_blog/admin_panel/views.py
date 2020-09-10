from django.shortcuts import render, redirect
from blog.views import Post
from .forms import EditPost, AddPostForms
# Create your views here.


def admin_panel(request):
    data = dict()
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-time_creation')
        data['posts'] = posts
        return render(request, 'blog/admin_panel.html', context=data)


def add_post(request):
    data = dict()
    if request.method == 'GET':
        add_post_form = AddPostForms()
        data['add_post_form'] = add_post_form
        return render(request, 'blog/add_post.html', context=data)
    elif request.method == 'POST':
        form = AddPostForms(request.POST, request.FILES)
        if form.is_valid():
            print('form')
            post = Post.objects.create(post_name=form.cleaned_data['post_name'],
                                    post=form.cleaned_data['post'],
                                    author=form.cleaned_data['author'],
                                    time_creation=form.cleaned_data['time_creation'],
                                    image=form.cleaned_data['image'])
            post.save()
        return redirect('/admin_panel')


def edit_post(request, iid: int):
    data = dict()
    post = Post.objects.get(id=iid)
    if request.method == 'GET':
        instans = EditPost(instance=post)
        data['edit_post_form'] = instans
        data['post'] = post
        return render(request, 'blog/edit_post.html', context=data)
    elif request.method == 'POST':
        form = EditPost(request.POST, request.FILES)
        if form.is_valid():
            post.post_name = form.cleaned_data['post_name']
            post.post = form.cleaned_data['post']
            post.author = form.cleaned_data['author']
            post.time_creation = form.cleaned_data['time_creation']
            post.time_publication = form.cleaned_data['time_publication']
            post.time_update = form.cleaned_data['time_update']
            post.image = form.cleaned_data['image']
            post.save()

        return redirect('/admin_panel')


def delete_post(request, iid: int):
    post = Post.objects.get(id=iid)
    post.delete()
    return redirect('/admin_panel')
