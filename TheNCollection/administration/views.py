from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Droid.models import Post
from userlogin.models import Profile
from userlogin.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@admin_only
def homepage(request):
    post = Post.objects.all()
    post_count = post.count()
    profile = Profile.objects.all()
    profile_count = profile.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'post': post_count,
        'profile': profile_count,
        'user': user_count,
        'admin': admin_count
    }

    return render(request, 'administration/adminhomepage.html', context)

@login_required
@admin_only
def get_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users':users
    }
    return render(request, 'administration/users.html', context)


@login_required
@admin_only
def get_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'admins':admins
    }
    return render(request, 'administration/admins.html', context)

@login_required
@admin_only
def promote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/admins')

@login_required
@admin_only
def demote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin demoted to user')
    return redirect('/admins/users')   

@login_required
@admin_only
def get_profile(request):
    profile = Profile.objects.filter().order_by('-id')
    context = {
        'profiles': profile
    }
    return render(request, 'administration/profile.html', context)

@login_required
@admin_only
def get_post(request):
    post = Post.objects.filter().order_by('-id')
    context = {
        'posts': post
    }
    return render(request, 'administration/post.html', context)

@login_required
@admin_only
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/administration/admins/getpost')    




