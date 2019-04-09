from django.contrib import admin

from .models import Toppings, Crust, Size, Flavour, Pizza, FlavourLReg, FlavourLSic, FlavourSSic, Cart, Sub
# thebigelephant
# Register your models here.

admin.site.register(Toppings)
admin.site.register(Crust)
admin.site.register(Size)
admin.site.register(Flavour)
admin.site.register(Pizza)
admin.site.register(FlavourLReg)
admin.site.register(FlavourLSic)
admin.site.register(FlavourSSic)
admin.site.register(Cart)
admin.site.register(Sub)