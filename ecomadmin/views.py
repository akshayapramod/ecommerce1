from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'ecomadmintemplates/login.html')
def home(request):
    return render(request,'ecomadmintemplates/home.html')
def approveseller(request):
    return render(request,'ecomadmintemplates/approveseller.html')
def viewseller(request):
    return render(request,'ecomadmintemplates/viewseller.html')
def viewcustomer(request):
    return render(request,'ecomadmintemplates/viewcustomer.html')
def viewsellerorders(request):
    return render(request,'ecomadmintemplates/viewsellerorders.html')