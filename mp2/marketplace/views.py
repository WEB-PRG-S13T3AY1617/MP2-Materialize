from django.shortcuts import render, get_object_or_404, redirect
from marketplace.forms import RegistrationForm, PostForm, OfferForm #, AcceptRejectForm
from django.contrib.auth.views import login
from .models import User, Post, Offer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    latest_post_list = Post.objects.all().order_by('-id')

    if request.user.is_authenticated():
        offers = Offer.objects.filter(user=request.user)
        offers2 = Offer.objects.filter(post__in=Post.objects.filter(user=request.user).order_by('-id'))
    else:
        offers = None
        offers2 = None

    search = request.GET.get('query')
    page = request.GET.get('page')
    itemnum = request.GET.get('c')

    if search:
        latest_post_list = latest_post_list.filter(tags__name__in=[search]).distinct()
    paginator = Paginator(latest_post_list, 10)

    if itemnum:
        paginator = Paginator(latest_post_list, itemnum)

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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'latest_post_list': latest_post_list,
                'regform': regform,
                'postform': postform,
                'offers': offers,
                'offers2': offers2,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        postform = PostForm()
        regform = RegistrationForm()
        try:
            latest_post_list = paginator.page(page)
        except PageNotAnInteger:
            latest_post_list = paginator.page(1)
        except EmptyPage:
            latest_post_list = paginator.page(paginator.num_pages)
        context = {
            'latest_post_list': latest_post_list,
            'regform': regform,
            'postform': postform,
            'offers': offers,
            'offers2': offers2,
        }
        return render(request, 'marketplace/index.html', context)


def userdetails(request, user_id):
    userobj = get_object_or_404(User, pk=user_id)
    user_latest_post = Post.objects.filter(user=userobj).order_by('-id')
    offers = Offer.objects.filter(post__in=user_latest_post).order_by('-id')
    myoffers = Offer.objects.filter(user=request.user, post__in=user_latest_post).order_by('-id')

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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'userprofile': userobj,
                'latest_posts': user_latest_post,
                'regform': regform,
                'postform': postform,
                'offers': offers,
                'myoffers': myoffers,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        context = {
            'userprofile': userobj,
            'latest_posts': user_latest_post,
            'regform': regform,
            'postform': postform,
            'offers': offers,
            'myoffers': myoffers,
        }
        return render(request, 'marketplace/user.html', context)


def makeoffer(request, post_id):
    userobj = request.user
    latest_post_list = Post.objects.filter(user=userobj).order_by('-id')
    postobj = Post.objects.filter(id=post_id)[:1].get()

    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        postform = PostForm(request.POST, request.FILES)
        offerform = OfferForm(request.POST)

        if offerform.is_valid():
            offerobj = offerform.save(commit=False)
            offerobj.user = request.user
            offerobj.post = Post.objects.filter(id=post_id)[:1].get()
            offerobj.save()
            return redirect('/')
        elif regform.is_valid():
            regform.save()
            return redirect('/')
        elif postform.is_valid():
            obj = postform.save(commit=False)
            obj.user = request.user
            obj.image = postform.cleaned_data['image']
            obj.save()
            postform.save_m2m()
            return redirect('/')
        else:
            postform = PostForm()
            regform = RegistrationForm()
            offerform = OfferForm()
            context = {
                'regform': regform,
                'postform': postform,
                'offerform': offerform,
                'posts': latest_post_list,
                'postobj': postobj,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        offerform = OfferForm()
        context = {
            'regform': regform,
            'postform': postform,
            'offerform': offerform,
            'posts': latest_post_list,
            'postobj': postobj,
        }
        return render(request, 'marketplace/offer.html', context)


def canceloffer(request, myoffer_id):
    myofferobj = Offer.objects.filter(id=myoffer_id)[:1].get()
    myofferobj.delete()
    return redirect('/')


def updateoffer(request, myoffer_id):
    myofferobj = Offer.objects.filter(id=myoffer_id)[:1].get()
    postobj = Post.objects.filter(id=myofferobj.post.id)[:1].get()
    myofferobj.delete()
    return redirect('/' + 'offer/' + str(postobj.id) + '/')


def approveoffer(request, offer_id):
    offerobj = Offer.objects.filter(id=offer_id)[:1].get()

    offerobj.approve_reject = True
    offerobj.reason = request.POST.get("reasonA", "")
    offerobj.save()
    return redirect('/')


def rejectoffer(request, offer_id):
    offerobj = Offer.objects.filter(id=offer_id)[:1].get()

    offerobj.approve_reject = False
    offerobj.reason = request.POST.get("reasonR", "")
    offerobj.save()
    return redirect('/')


def photo(request, post_id):
    postobj = Post.objects.filter(id=post_id)
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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'post': postobj,
                'regform': regform,
                'postform': postform,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        context = {
            'post': postobj,
            'regform': regform,
            'postform': postform,
        }
        return render(request, 'marketplace/image.html', context)


def condresults(request, condition_name):
    postobj = Post.objects.filter(condition=condition_name)
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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'query_item': condition_name,
                'post': postobj,
                'regform': regform,
                'postform': postform,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        context = {
            'query_item': condition_name,
            'post': postobj,
            'regform': regform,
            'postform': postform,
        }
        return render(request, 'marketplace/results.html', context)


def typeresults(request, type_name):
    postobj = Post.objects.filter(type=type_name)
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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'query_item': type_name,
                'post': postobj,
                'regform': regform,
                'postform': postform,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        context = {
            'query_item': type_name,
            'post': postobj,
            'regform': regform,
            'postform': postform,
        }
        return render(request, 'marketplace/results.html', context)


def courseresults(request, course_name):
    postobj = Post.objects.filter(course=course_name)
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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'query_item': course_name,
                'post': postobj,
                'regform': regform,
                'postform': postform,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        context = {
            'query_item': course_name,
            'post': postobj,
            'regform': regform,
            'postform': postform,
        }
        return render(request, 'marketplace/results.html', context)


def tagresults(request, tag_name):
    postobj = Post.objects.filter(tags__name__in=[tag_name]).distinct()
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
            postform = PostForm()
            regform = RegistrationForm()
            context = {
                'query_item': tag_name,
                'post': postobj,
                'regform': regform,
                'postform': postform,
            }
            return login(request, context, template_name='marketplace/err.html')
    else:
        regform = RegistrationForm()
        postform = PostForm()
        context = {
            'query_item': tag_name,
            'post': postobj,
            'regform': regform,
            'postform': postform,
        }
        return render(request, 'marketplace/results.html', context)
