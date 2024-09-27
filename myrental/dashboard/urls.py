
from django.contrib import admin
from django.urls import path
from .import views
from .views import Upsert3D
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("overview/", views.overview, name="overview"),
    path("tenants/", views.tenants, name="tenants"),
    path("rental/", views.rental, name="rental"),
    path("3Dmodels/", views.rental_model, name="3Dmodels"),
    path('dashboard/3Dmodels/add/', Upsert3D, name='3DmodelsUpsert'),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
