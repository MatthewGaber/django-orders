from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Toppings, Crust, Size, Flavour, FlavourLReg, FlavourLSic, FlavourSSic

# Create your views here.
def index(request):
    pizza = Pizza.objects.get(pk=2)
    context = {
        "pizzasex": pizza,
        "toppingsex": pizza.toppings.all(),
        "topping": Toppings.objects.all(),
        "crust": Crust.objects.all(),
        "size": Size.objects.all(),
        "flavour": Flavour.objects.all(),
        "flavourlreg": FlavourLReg.objects.all(),
        "flavourlsic": FlavourLSic.objects.all(),
        "flavourssic": FlavourSSic.objects.all()

    }
    return render(request, "index.html", context)

def addpizza(request, t, c, s, f):
    print(t)
