from django.contrib import admin

# Register your models here.
from shop.models import Shop, Menu

admin.site.register(Shop)
admin.site.register(Menu)
