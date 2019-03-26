from django.contrib import admin
from mapping.models import Data1

class Data1Admin(admin.ModelAdmin):
    list_per_page=10




admin.site.register(Data1,Data1Admin)
# Register your models here.
