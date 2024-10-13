# myApp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myApp.models import User, Model, Tenant,RentalSpaces  # Ensure your models are imported

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['rental_space', 'file_path', 'uploaded_by']


class TenantForm(forms.ModelForm):

    class Meta:
         
         model= Tenant
         fields= ['user','lease_start_date','lease_end_date','rental_space','monthly_rent','payment_status']


class RentalSpaceForm(forms.ModelForm):

    class Meta:
        model= RentalSpaces
        fields= ['name','description','price','status','dimensions','location','model_path',]

class LoginForm(AuthenticationForm): 
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])  # Set password correctly
        
        if commit:
            user.save()
        
        return user

     
       