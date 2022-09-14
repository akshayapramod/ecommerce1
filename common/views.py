from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'commontemplates/index.html')
def sellerlogin(request):
    return render(request,'commontemplates/sellerlogin.html')
def customerlogin(request):
    return render(request,'commontemplates/customerlogin.html')
def sellersignup(request):
    return render(request,'commontemplates/sellersignup.html')
def customersignup(request):
    return render(request,'commontemplates/customersignup.html')
def changepassword(request):
    return render(request,'commontemplates/changepassword.html')
def image(request):
    return render(request,'commontemplates/image.html') 
    

    