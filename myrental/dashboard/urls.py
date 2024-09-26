
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("overview/", views.overview, name="overview"),
    path("tenants/", views.tenants, name="tenants"),
    path("rental/", views.rental, name="rental"),
     path("3Dmodels/", views.rental_model, name="3Dmodels"),
  
]
