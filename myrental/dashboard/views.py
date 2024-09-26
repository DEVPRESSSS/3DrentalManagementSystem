from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import *
# Create your views here.
def dashboard(request):

    return render(request,"dashboard/dash_base.html")

def overview(request):

    return render(request,"dashboard/overview.html")

def tenants(request):

    tenants_list = Tenant.objects.all()

    return render(request,"dashboard/tenants.html",{"tenants_list":tenants_list})

def rental(request):
    rental_list = RentalSpaces.objects.all()
    return render(request,"dashboard/rentals.html",{"rental_list":rental_list})


def rental_model(request):
    rental_list_model = Model.objects.all()
    print(rental_list_model)
    return render(request,"dashboard/3Dmodels.html",{"rental_list_model":rental_list_model})