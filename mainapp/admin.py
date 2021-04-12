from django.contrib import admin
from .models import Products
from django.contrib.auth import get_user_model


admin.site.register(Products)
admin.site.register(get_user_model())