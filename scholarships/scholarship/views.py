from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import Http404
from django.views import generic
from django.utils import timezone
from django.contrib import auth
from django.core.context_processors import csrf
from scholarship.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from .models import Userprofile
from .models import options

# Create your views here.

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            my_user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],)
            #profile = my_user.get_profile()
            my_user.userprofile.age = form.cleaned_data['age']
            my_user.userprofile.category = form.cleaned_data['category']
            my_user.userprofile.state = form.cleaned_data['state']
            
            my_user.userprofile.save()
            my_user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    querylist = options.objects.filter(option_state=request.user.userprofile.state).filter(option_category=request.user.userprofile.category)

    return render_to_response(
    'home.html',
    { 'user': request.user,
    'query_list':querylist }
    )