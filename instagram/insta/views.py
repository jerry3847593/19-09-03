from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like, Comment, User
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
import operator



def main(request):
    posts = Post.objects.all()
    sort = request.GET.get("sort", "")
    comment_form = CommentForm

    if sort == "new":
        posts = Post.objects.all()
    elif sort == "like":
        ordered_posts = {}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key = operator.itemgetter(1), reverse=True)
        posts = []
        for post in post_list:
            posts.append(post[0])
    elif sort == "like2":
        ordered_posts = {}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key = operator.itemgetter(1), reverse=False)
        posts = []
        for post in post_list:
            posts.append(post[0])
        
    try:
        liked_post = Like.objects.filter(user=request.user).values_list('post__id', flat=True)
    except:
        liked_post = None

    return render(request, 'insta/main.html',{'posts':posts, 'liked_post':liked_post, 'comment_form':comment_form,})
            
    

@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
        except:
            Like.objects.create(user=request.user, post=post)

    return redirect('main')

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main')
    else:
        form = PostForm
    return render(request, 'insta/post_created.html', {'form':form})

def edit(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main')
    else:
        form = PostForm(instance= post)
    return render(request, 'insta/post_edit.html', {'form':form})

def delete(request, post_pk):
    post = get_object_or_404(Post, pk= post_pk)
    post.delete()
    return redirect('main')

def create_comment(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            return redirect('main')

def comment_edit(request, post_pk):
    comment = get_object_or_404(Post, pk = post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('main')
    else:
        form = CommentForm(instance = comment)
    return render(request, 'insta/comment_edit.html', {'form':form})

def comment_delete(request, post_pk):
    comment = get_object_or_404(Post, pk= post_pk)
    comment.delete()
    return redirect('main')


