
from django.contrib import admin #fron importa los modulos
from django.urls import path, include



urlpatterns = [ #es una lista que contiene las rutas de urñ
    path("admin/", admin.site.urls),#define las rutas de url
    path("", include('base.urls')),
    
]
