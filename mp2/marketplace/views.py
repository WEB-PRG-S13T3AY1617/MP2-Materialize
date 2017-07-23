from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User, Post


def index(request):
    latest_post_list = Post.objects.order_by('-id')[:10]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'marketplace/index.html', context)


def userdetails(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'marketplace/user.html', {'user': user})


def registration(request):
    return render(request, 'marketplace/registration.html')
