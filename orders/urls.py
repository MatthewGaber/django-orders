from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getmodel", views.getmodel, name="getmodel"),
    path("addpizza", views.addpizza, name = "addpizza"),
    path("addsub", views.addsub, name = "addsub"),
    path("addpasta", views.addpasta, name = "addpasta"),
    path("addsalad", views.addsalad, name = "addsalad"),
    path("addplatter", views.addplatter, name = "addplatter"),
    path("checkout/", views.checkout, name = "checkout")
]
