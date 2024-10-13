
from django.contrib import admin
from django.urls import path
from .import views
from .views import Upsert3D, EditModel, DeleteModel, AddTenant, DeleteTenant, EditTenant, AddRentalSpace
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("overview/", views.overview, name="overview"),
    path("tenants/", views.tenants, name="tenants"),
    path("rental/", views.rental, name="rental"),
    path("3Dmodels/", views.rental_model, name="3Dmodels"),
    path('dashboard/3Dmodels/add/', Upsert3D, name='3DmodelsUpsert'),
    path('dashboard/3Dmodels/edit/<int:id>/', EditModel, name='EditModel'),
    path('dashboard/3dmodels/delete/<int:id>/',DeleteModel, name='DeleteModel'),
    path('dashboard/tenants/add/',AddTenant, name='AddTenant'),
    path('dashboard/tenants/delete/<int:id>/',DeleteTenant, name='DeleteTenant'),
    path('dashboard/tenants/edit/<int:id>/', EditTenant, name='EditTenant'),
    path('dashboard/rental/add/', AddRentalSpace, name='AddRentalSpace'),


]

