from django.contrib import admin
from . import models
# Register your models here.


class Hospitaladmin(admin.ModelAdmin):
    list_display = ['id','name','speciality']


# admin.site.register(Hosp)
admin.site.register(models.Hosp, Hospitaladmin)