from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/add/', views.ProductCreateView.as_view()),
    path('products/view/', views.ProductListView.as_view()),
    path('account/login/', views.login, name='login'),
    path('account/signup/', views.signup, name='signup'),
    path('account/logout/', views.auth_logout, name='logout'),
    path('products/add/file', views.ProductWithFile, name='productfile'),
    path('products/<id>/', views.ProductDetailPage, name='productdetail'),
    path('sponsor/', views.gitSponsor, name='gitsponsor'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]