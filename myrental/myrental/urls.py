
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myApp.urls")),
    path('__debug__/',include(debug_toolbar.urls)),
    path('dashboard/', include("dashboard.urls"))
]
