from django.urls import path
from . import views

urlpatterns=[
    path('customerhome',views.customerhome),
    path('productdetails',views.productdetails),
    path('viewcart',views.viewcart),
    path('myoders',views.myorders),
    path('changepassword',views.changepassword)

]