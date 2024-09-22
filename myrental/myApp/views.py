from django.shortcuts import render
from .models import RentalSpaces,Tenant,Payment,Model
def home(request):

    rentals_space = RentalSpaces.objects.filter(status="Available")
    
    return render(request, "myapp/Home.html", {'rentalspace': rentals_space})  


def login(request):

    return render (request,"myapp/login.html")

def rentalspace(request):

    rentals_space = RentalSpaces.objects.filter(status="Available")
    
    return render(request, "myapp/rentalspaceavailable.html", {'rentalspace': rentals_space}) 

def rentalspaceview(request,id):

    space = RentalSpaces.objects.get(space_id=id)
    return render(request, "myapp/rentalspaceview.html", {'space': space})
def about(request):

    return render (request,"myapp/about.html")

def contact(request):

    return render (request,"myapp/contact.html")


