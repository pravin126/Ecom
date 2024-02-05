from django.contrib import admin

from .models import category,subcategory,product

admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(product)
