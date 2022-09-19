from django.shortcuts import render

# Create your views here.
def customerhome(request):
    return render(request,'customertemplates/customerhome.html')
def productdetails(request):
    return render(request,'customertemplates/productdetails.html')
def viewcart(request):
    return render(request,'customertemplates/viewcart.html')    
def myorders(request):
    return render(request,'customertemplates/myorders.html')
def changepassword(request):
    return render(request,'customertemplates/changepassword.html')
def img(request):
    return render(request,'customertemplates/img.html')    

    


    