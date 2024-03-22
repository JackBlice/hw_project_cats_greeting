from django.contrib import admin
from shop.models import Item, Clients, Purchase


# Register your models here.
admin.site.register(Item)
admin.site.register(Clients)
admin.site.register(Purchase)