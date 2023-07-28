from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('CrudProject1.urls')),
]
