from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getmodel", views.getmodel),
    path("addpizza", views.addpizza)
]
