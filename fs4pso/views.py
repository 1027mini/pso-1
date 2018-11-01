from __future__ import unicode_literals
from django import forms
from .forms import PostForm, CommentForm, SignupForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Subject, Comment, User

def write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            '''post.name = request.name
            post.subject = request.subject
            post.good_points = request.good_points
            post.improving_points = request.improving_points
            post.another_points = request.another_points'''
            post.created_date = timezone.now()
            post.save()
            return redirect('main_subject')
    else:
        form = PostForm()
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/write.html', {'form': form, 'subjects': subjects})

def main_subject(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse()
    return render(request, 'fs4pso/main.html', {'subjects': subjects, 'posts': posts})

def subject(request, subject_id):
     subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
     posts = Post.objects.filter(created_date__lte=timezone.now(), subject = subject_id).order_by('created_date').reverse()
     return render(request, 'fs4pso/main.html', {'subjects': subjects, 'posts': posts})

#def main_post(request):
#    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse()
#    return render(request, 'fs4pso/main_block_content.html', {'posts': posts})

def login(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/login.html', {'subjects': subjects})

def terms(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/terms_of_use.html', {'subjects': subjects})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.save()
            return redirect('/login')
    else:
        form = SignupForm()
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    users =  User.objects.filter()
    return render(request, 'fs4pso/signup.html', {'subjects': subjects, 'users': users, 'form': form})

def find(request):
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'fs4pso/find.html', {'subjects': subjects})

#def look(request):
#    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
#    return render(request, 'fs4pso/look.html', {'subjects': subjects})

def looks(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id = post_id)
            #comment.name = request.name
            comment.created_date = timezone.now()
            comment.save()
            return redirect('/look/{}'.format(post_id))
    else:
        form = CommentForm()
    subjects = Subject.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.filter(id = post_id)
    comments = Comment.objects.filter(post = post_id).order_by('created_date').reverse()
    return render(request, 'fs4pso/look2.html', {'posts' : posts, 'subjects': subjects, 'comments' : comments, 'form': form })

def likes(request, post_id):
    post = Post.objects.get(id = post_id)
    post.num_of_likes += 1
    post.save(update_fields=['num_of_likes'])
    return HttpResponseRedirect("/look/{}".format(post.id))
