from django.contrib import admin

from .models import LastUpdated, Duty, Product

admin.site.register(LastUpdated)
admin.site.register(Duty)
admin.site.register(Product)
