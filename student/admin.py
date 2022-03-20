from django.contrib import admin
from .models import customer_info

# Register your models here.
@admin.register(customer_info)

class UserAdmin (admin.ModelAdmin):
    list_display=['customer_id', 'customer_name','customer_org', 'email', 'NID', 'phone']
    