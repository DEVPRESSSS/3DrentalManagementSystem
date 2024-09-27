from . import views
from django.urls import path


urlpatterns= [

    path("",views.home, name="home"),
    path("login/",views.login, name="login"),
    path("rentalspace/",views.rentalspace, name="rentalspace"),
    path("contact/",views.contact, name="contact"),
    path("about/",views.about, name="about"),
    path('rentalspaceview/<int:id>/', views.rentalspaceview, name='rentalspaceview'),
    path("login/",views.login, name="login"),
]