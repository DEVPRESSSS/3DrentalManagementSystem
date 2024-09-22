from django.db import models

# Create your models here.

class User(models.Model):
    USER_ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.BinaryField()  
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class RentalSpaces(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
    ]
    
    space_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  
    dimensions = models.CharField(max_length=100, blank=True, null=True)  
    location = models.CharField(max_length=255, blank=True, null=True)  
    model_path = models.CharField(max_length=255, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
class Tenant(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    tenant_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    rental_space = models.ForeignKey('RentalSpaces', on_delete=models.CASCADE)  # Foreign key to RentalSpaces
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Tenant {self.tenant_id}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE)  # Foreign key to Tenant model
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.payment_id}"


class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    rental_space = models.ForeignKey('RentalSpaces', on_delete=models.CASCADE)  # Foreign key to RentalSpaces
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


