from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models import *
from dashboard.forms import ModelForm
from django.contrib import messages

# Create your views here.



#Render the dashboard 
def dashboard(request):

    return render(request,"dashboard/dash_base.html")

#Render the Overview.html

def overview(request):

    return render(request,"dashboard/overview.html")

#Render the tenants.html

def tenants(request):

    tenants_list = Tenant.objects.all()

    return render(request,"dashboard/tenants.html",{"tenants_list":tenants_list})

#renders the rentals.html

def rental(request):
    rental_list = RentalSpaces.objects.all()
    return render(request,"dashboard/rentals.html",{"rental_list":rental_list})

#renders the 3Dmodels.html

def rental_model(request):
    rental_list_model = Model.objects.all()
    return render(request,"dashboard/3Dmodels.html",{"rental_list_model":rental_list_model})


#renders add update 
def Upsert3D(request):


    if request.method == 'POST':
         
         form = ModelForm(request.POST,request.FILES)
         if form.is_valid():
              
              form.save()
              messages.success(request, '3D Model added successfully!')
              return redirect('3Dmodels')
         else:
            messages.error(request, 'Error adding the model. Please check the form.')
    else:
             
              form= ModelForm()

    return render(request, "dashboard/Upsert3D.html", {'form': form})
