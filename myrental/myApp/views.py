from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login  as auth_login  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import RentalSpaces,Tenant,Payment,Model, User
from dashboard.forms import RegistrationForm, LoginForm


def home(request):
    rentals_spaces = RentalSpaces.objects.filter(status="Available")
    
    rental_space_models = Model.objects.filter(rental_space__in=rentals_spaces)
    
    return render(request, "myapp/Home.html", {'rentalspaces': rentals_spaces, 'rental_space_models': rental_space_models})
 



#Render login logic
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_superuser:

                     return redirect('dashboard') 
                elif user.role == "Tenant":
                    return redirect ('contact') 
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'myApp/login.html', {'form': form})


#Render register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Set the role to 'Customer' before saving
            user = form.save(commit=False)
            user.role = 'User'
            user.save()

            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'myApp/register.html', {'form': form})


#Render rentalspace
def rentalspace(request):

    rentals_space = RentalSpaces.objects.filter(status="Available")
    
    return render(request, "myapp/rentalspaceavailable.html", {'rentalspace': rentals_space}) 

#Render rentalspaceview
def rentalspaceview(request,id):

    space = RentalSpaces.objects.get(space_id=id)
    rental_space_models = Model.objects.filter(rental_space=space)

    return render(request, "myapp/rentalspaceview.html", {'space': space, 'rental_space_models': rental_space_models})


#Render about
def about(request):

    return render (request,"myapp/about.html")

#Render contact
def contact(request):

    return render (request,"myapp/contact.html")

def dashboard(request):


    return render (request, "dashboard/dash_base.html")

