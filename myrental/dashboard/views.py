from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from myApp.models import *
from dashboard.forms import ModelForm, TenantForm,RentalSpaceForm
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


#renders the virtualtour.html

def virtualtour(request):
     

        return render(request,'dashboard/VirtualTourIndex.html')



#renders the rentals.html
def rental(request):
    rental_list = RentalSpaces.objects.all()
    return render(request,"dashboard/rentals.html",{"rental_list":rental_list})


#Add new rental space
def AddRentalSpace(request):

    if request.method == 'POST':
         
         form = RentalSpaceForm(request.POST)

         if form.is_valid():
              
              
              form.save()
           
              messages.success(request, 'New rental space added successfully!')
              return redirect('rental')
         else:
            messages.error(request, 'Error adding the rental. Please check the form.')
            print(f"{form.errors}")
    else:
             
              form= RentalSpaceForm()

    return render (request,"dashboard/AddRentalSpace.html",{'form': form})


def DeleteRental(request, id):
     
    model_instance = get_object_or_404(RentalSpaces, space_id= id)

    if model_instance:
         
        model_instance.delete()

        messages.success(request,'Rental Space deleted successfully')

    return redirect('rental')

def EditRental(request, id):
     
    my_model_instance = get_object_or_404(RentalSpaces, space_id=id)

    rental_space = RentalSpaces.objects.all()


   
    if request.method == 'POST':
        form = RentalSpaceForm(request.POST, instance=my_model_instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, f"Rental {id} updated successfully")
            return redirect('rental')
        else:
            messages.error(request, 'Error updating the rental. Please check the form.')

    else:
        form = RentalSpaceForm(instance=my_model_instance)

    return render(request, "dashboard/EditRental.html", {'form': form, 
                                                        'space_id': id,
                                                        'rental_space':rental_space

                                                        })


#renders the 3Dmodels.html

def rental_model(request):
    rental_list_model = Model.objects.all()
    return render(request,"dashboard/3Dmodels.html",{"rental_list_model":rental_list_model})


#renders add Model
def Upsert3D(request):


    if request.method == 'POST':
         
         form = ModelForm(request.POST,request.FILES)

         if form.is_valid():
              
              form.save()
              messages.success(request, 'New Model added successfully!')
              return redirect('3Dmodels')
         else:
            messages.error(request, 'Error adding the model. Please check the form.')
    else:
             
              form= ModelForm()
              form.fields['uploaded_by'].queryset = User.objects.filter(is_superuser=True)

    return render(request, "dashboard/InsertModel.html", {'form': form})


#Edit Model
def EditModel(request, id):
    my_model_instance = get_object_or_404(Model, model_id=id)

    rental_space = RentalSpaces.objects.all()
    users = User.objects.all()


   
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES, instance=my_model_instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, f"Model {id} updated successfully")
            return redirect('3Dmodels')
        else:
            messages.error(request, 'Error updating the model. Please check the form.')

    else:
        form = ModelForm(instance=my_model_instance)

    return render(request, "dashboard/EditModel.html", {'form': form, 
                                                        'model_id': id,
                                                        'rental_space':rental_space,
                                                        'users':users})


#Delete Model

def DeleteModel(request, id):


    model_stance = get_object_or_404(Model, model_id=id)

    if model_stance:

        model_stance.delete()
        messages.success(request, ' Model deleted successfully!')

    
    return redirect('3Dmodels')








  
#Add Tenant

def AddTenant(request):
    if request.method == 'POST':
         
         form = TenantForm(request.POST,request.FILES)

         if form.is_valid():
              
              form.save()
              rental_space_id = form.cleaned_data['rental_space'].space_id

              rental_space = get_object_or_404(RentalSpaces, space_id=rental_space_id)

              rental_space.status = 'Occupied'  
              rental_space.save()

              user_ids = form.cleaned_data['user'].user_id

              tenant_obj= get_object_or_404(User,user_id = user_ids)

              tenant_obj.role= 'Tenant'

              tenant_obj.save()




              messages.success(request, 'New Tenant added successfully!')

             
              return redirect('tenants')
         else:
            messages.error(request, f'Error adding the model. Please check the form.')

            print(f"{form.errors}")
    else:
             
              form= TenantForm()
              form.fields['user'].queryset = User.objects.filter(is_superuser=False, is_staff=False, role= 'User')
              form.fields['rental_space'].queryset = RentalSpaces.objects.filter(status= 'Available')


    return render(request, "dashboard/AddTenant.html",{'form':form})


def EditTenant(request, id):
    my_model_instance = get_object_or_404(Tenant, tenant_id=id)

    tenant = Tenant.objects.all()
    rental_space = RentalSpaces.objects.all()

   
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=my_model_instance)
        
        if form.is_valid():
            form.save()
            messages.success(request, f"Tenants {id} updated successfully")
            return redirect('tenants')
        else:
            messages.error(request, 'Error updating the model. Please check the form.')

    else:
        form = TenantForm(instance=my_model_instance)
        form.fields['user'].queryset = User.objects.filter(is_superuser=False, is_staff=False)

    return render(request, "dashboard/EditTenant.html", {'form': form, 
                                                        'tenant_id': id,
                                                        'tenant':tenant,
                                                        'rental_space':rental_space
                                                       })



#Delete Tenant
def DeleteTenant(request,id):
     
    model_stance = get_object_or_404(Tenant, tenant_id=id)

    if model_stance:

        model_stance.delete()
        messages.success(request, ' Tenant deleted successfully!')

    else:

        print(f"{model_stance}")

    
    return redirect('tenants')





     