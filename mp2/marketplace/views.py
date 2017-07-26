from django.shortcuts import render, get_object_or_404, redirect
from marketplace.forms import RegistrationForm
from .models import User, Post


def index(request):
    latest_post_list = Post.objects.order_by('-id')[:10]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'marketplace/index.html', context)


def userdetails(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'marketplace/user.html', {'userprofile': user})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(request, 'marketplace/reg_form.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'marketplace/reg_form.html', args)
