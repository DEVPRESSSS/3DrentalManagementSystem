from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import RentalSpaces, Tenant, Payment, Model,UserManager,User

# Register your models here.
admin.site.register(RentalSpaces)
admin.site.register(Tenant)
admin.site.register(Payment)
admin.site.register(Model)
admin.site.register(User)


