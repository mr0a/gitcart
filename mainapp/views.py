from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .models import Products
from django.template import loader
from django.http import HttpResponse
from django import template

import json


def index(req):
    queryset = Products.objects.all()
    cities = Products.objects.order_by().values('origin').distinct()
    ctx = {'cities': cities}
    if req.GET.get('city'):
        city = req.GET.get('city')
        city_product = Products.objects.filter(origin=city)
        ctx['products'] = city_product
        return render(req, 'mainapp/index.html', context=ctx)
    value = len(queryset) - len(queryset)%3
    ctx['products'] = queryset[0:value]
    return render(req, 'mainapp/index.html', context=ctx)


class ProductCreateView(CreateView):
    model = Products
    fields = '__all__'

class ProductListView(ListView):
    queryset = Products.objects.all()
    context_object_name = 'products'


def ProductWithFile(req):
    if req.POST and req.FILES:
        jsonfile = req.FILES.get('file')
        jsondata = json.load(jsonfile)
        for data in jsondata:
            # print(data)
            Products.objects.create(title=data['ProName'], product_type=data['ProType'],
                                    description=data['Desc'], price=data['Price'], image=data['image'], origin=data['Origin'])
        return redirect('index')


def ProductDetailPage(req, id):
    cities = Products.objects.order_by().values('origin').distinct()
    ctx = {'cities': cities}
    product = Products.objects.filter(id=id)
    ctx['product'] =  product[0]
    return render(req, 'mainapp/product_page.html', context=ctx)

def gitSponsor(req):
    return render(req, 'sponsor/sponsor.html')

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        load_template = 'sponsor/' + load_template
        print(load_template)
        # context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


from django.contrib.auth import authenticate, get_user_model, logout, login as auth_login
from django.contrib.auth.views import LoginView

from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'mainapp/signup.html'

class MyLoginView(LoginView):
    template_name = 'mainapp/login.html'

def login(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'POST':
        print(req.POST)
        user = authenticate(req, username=req.POST.get('email'), password=req.POST.get('password'), name='Demo')
        print(user)
        if user is not None:
            auth_login(req, user)
            return redirect('index')
    return render(req, 'mainapp/login.html')


def signup(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'POST':
        user_model = get_user_model()
        user = user_model.objects.create(name=req.POST.get('name'), email=req.POST.get('email'), password = req.POST.get('password1'))
        print(user)
        return redirect('login')
    return render(req, 'mainapp/signup.html')

def auth_logout(req):
    if req.user.is_authenticated:
        logout(req)
    return redirect('index')