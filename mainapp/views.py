from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .models import Products

import json


def index(req):
    queryset = Products.objects.all()
    value = len(queryset) - len(queryset)%3
    ctx = {'products': queryset[0:value]}
    print(ctx)
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
    product = Products.objects.filter(id=id)
    # print(dict(product[0]))
    ctx = {'product': product[0]}
    return render(req, 'mainapp/product_page.html', context=ctx)
