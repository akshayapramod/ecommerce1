from django.shortcuts import render

# Create your views here.
def sellerhome(request):
    return render(request,'sellertemplates/sellerhome.html')
def cost(request):
    return render(request,'sellertemplates/cost.html')
def myorders(request):
    return render(request,'sellertemplates/myorders.html')
def addproduct(request):
    return render(request,'sellertemplates/addproduct.html')
def changepassword(request):
    return render(request,'sellertemplates/changepassword.html')
def updatestock(request):
    return render(request,'sellertemplates/updatestock.html')


