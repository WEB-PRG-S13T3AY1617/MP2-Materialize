from django.shortcuts import render, get_object_or_404, redirect
from marketplace.forms import RegistrationForm, PostForm
from django.contrib.auth.views import login
from .models import User, Post


def index(request):
    latest_post_list = Post.objects.order_by('-id')
    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        postform = PostForm(request.POST, request.FILES)
        if regform.is_valid():
            regform.save()
            return redirect('/')
        elif request.user.is_authenticated():
            if postform.is_valid():
                obj = postform.save(commit=False)
                obj.user = request.user
                obj.image = postform.cleaned_data['image']
                obj.save()
                postform.save_m2m()
                return redirect('/')
        else:
            context = {
                'latest_post_list': latest_post_list,
                'regform': regform,
                'postform': postform,
            }
            return login(request, context, template_name='index')
    else:
        postform = PostForm()
        regform = RegistrationForm()
        context = {
            'latest_post_list': latest_post_list,
            'regform': regform,
            'postform': postform,
        }
        return render(request, 'marketplace/index.html', context)


def userdetails(request, user_id):
    userobj = get_object_or_404(User, pk=user_id)
    user_latest_post = Post.objects.filter(user=userobj).order_by('-id')
    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        if regform.is_valid():
            regform.save()
            return redirect('/')
        else:
            context = {
                'userprofile': userobj,
                'latest_posts': user_latest_post,
                'regform': regform,
            }
            return login(request, context, template_name='userdetails')
    else:
        regform = RegistrationForm()
        context = {
            'userprofile': userobj,
            'latest_posts': user_latest_post,
            'regform': regform,
        }
        return render(request, 'marketplace/user.html', context)
