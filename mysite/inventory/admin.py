from django.contrib import admin

from inventory.models import Item, Company

admin.site.register(Item)
admin.site.register(Company)
