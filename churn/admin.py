from django.contrib import admin
from .models import Data, Back

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('tenure', 'seniorCitizen', 'partner', 'dependents', 'phone_service', 'internet_service', 'charges', 'contract', 'payment_method', 'predictions')
admin.site.register(Data, DataAdmin)
admin.site.register(Back)