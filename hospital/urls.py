from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("hospital/", views.pathHospital, name="pathHospital"), # this will show all hospitals as per query
    path("hospital/<int:myid>", views.getHospitalbyid, name="getHospitalbyid"),

]