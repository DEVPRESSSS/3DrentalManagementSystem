from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator  

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Tenant', 'Tenant'),
        ('User','User')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='User')
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class RentalSpaces(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Booked', 'Booked'),
    ]
    
    space_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  
    dimensions = models.CharField(max_length=100, blank=True, null=True)  
    location = models.CharField(max_length=255, blank=True, null=True)
    amenities = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
    


    
class Tenant(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    tenant_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE) 
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    rental_space = models.ForeignKey('RentalSpaces', on_delete=models.CASCADE) 
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Tenant {self.tenant_id}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE)  
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.payment_id}"


class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    rental_space = models.ForeignKey('RentalSpaces', on_delete=models.CASCADE)  
    file_path = models.ImageField(upload_to='images/')
    three_path = models.FileField(
        upload_to='3Dfiles/', 
        validators=[FileExtensionValidator(allowed_extensions=['glb'])],
        blank=True,  
        null=True    
    )
    uploaded_by = models.ForeignKey('User',  on_delete=models.SET_NULL, null=True, blank=True)  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_path.name

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  
    rental_space = models.ForeignKey('RentalSpaces', on_delete=models.CASCADE) 
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    booking_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending')  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.booking_id} for {self.user.username}"
