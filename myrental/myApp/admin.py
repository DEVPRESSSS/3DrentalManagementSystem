from django.contrib import admin
from django.contrib.auth.models import User
from .models import RentalSpaces,Tenant,Payment,Model

# Register your models here.
admin.site.register(RentalSpaces)
admin.site.register(Tenant)
admin.site.register(Payment)
admin.site.register(Model)
admin.site.unregister(User)


