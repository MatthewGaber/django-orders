from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from .forms import SignupForm
from django.http import JsonResponse

from .models import Pizza, Toppings, Crust, Size, Flavour, FlavourLReg, FlavourLSic, FlavourSSic

# Create your views here.
def index(request):
    pizza = Pizza.objects.get(pk=2)
    fl = FlavourLSic.objects.all()
    #fls = json.dumps(list(fl), cls=DjangoJSONEncoder)
    #fls = json.dumps(fl)
    fls = serializers.serialize('json', fl)
    form = SignupForm()
    context = {
        "form": form,
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

def getmodel(request):
    size = request.GET.get('size', None)
    print(size)
    if size == 'Small':
        data = serializers.serialize('json', FlavourSSic.objects.all())
        return HttpResponse(data, content_type="application/json")
    else:
        data = serializers.serialize('json', FlavourLSic.objects.all())
        return HttpResponse(data, content_type="application/json")

    
        

def addpizza(request):
    if request.method == 'POST':
        toppings = request.POST['topping']
        size = request.POST['size']
        crust = request.POST['crust']
        flavour = request.POST['flavmodel']
        print(toppings)
        print(size)
        print(crust)
        print(flavour)
    newPizza = Pizza.objects.create(
        size = Size.objects.get(pk=size),
        crust = Crust.objects.get(pk=crust),
        flavoursr = Flavour.objects.get(pk=flavour)
    )
    newPizza.toppings.add(Toppings.objects.get(pk=toppings))


    return HttpResponse('wtf', content_type="application/json")
