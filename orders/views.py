from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    pizza = Pizza.objects.get(pk=1)
    context = {
        "pizzas": pizza,
        "toppings": pizza.toppings.all()

    }
    return render(request, "index.html", context)
