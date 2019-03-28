from django.contrib import admin

from .models import Toppings, Crust, Size, Flavour, Pizza
# thebigelephant
# Register your models here.
admin.site.register(Toppings)
admin.site.register(Crust)
admin.site.register(Size)
admin.site.register(Flavour)
admin.site.register(Pizza)