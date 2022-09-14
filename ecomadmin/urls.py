from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login),
    path('home',views.home),
    path('approveseller',views.approveseller),
    path('viewseller',views.viewseller),
    path('viewcustomer',views.viewcustomer),
    path('viewsellerorders',views.viewsellerorders)


]