from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    
    return render(request,"index.html")

def aboutus(request):
    
    return render(request,"aboutus.html")


def house(request):
    
    return render(request,"house.html")

def land(request):
    
    return render(request,"land.html")
def post(request):
    
    return render(request,"post-property.html")