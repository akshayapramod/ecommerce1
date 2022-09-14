from django.urls import path
from . import views

urlpatterns=[
    path('sellerhome',views.sellerhome),
    path('cost',views.cost),
    path('myorders',views.myorders),
    path('addproduct',views.addproduct),
    path('changepassword',views.changepassword),
    path('updatestock',views.updatestock)

    
    
    
    ]