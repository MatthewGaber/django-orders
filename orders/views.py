from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
#from .forms import LargeSicilian, SmallSicilian
from django.http import JsonResponse
from django.contrib.auth.models import User



from .models import Pizza, Toppings, Crust, Size, Flavour, FlavourLReg, FlavourLSic, FlavourSSic, Cart, Sub

# Create your views here.
def index(request):
    #pizza = Pizza.objects.get(pk=2)
    #fl = FlavourLSic.objects.all()
    #fls = json.dumps(list(fl), cls=DjangoJSONEncoder)
    #fls = json.dumps(fl)
    #fls = serializers.serialize('json', fl)
    #form = SmallSicilian()
    context = {
        #"form": form,
        #"pizzasex": pizza,
        #"toppingsex": pizza.toppings.all(),
        "topping": Toppings.objects.all(),
        "crust": Crust.objects.all(),
        "size": Size.objects.all(),
        "flavour": Flavour.objects.all(),
        "flavourlreg": FlavourLReg.objects.all(),
        "flavourlsic": FlavourLSic.objects.all(),
        "flavourssic": FlavourSSic.objects.all(),
        "subs": Sub.objects.all()

    }
    return render(request, "orders/index.html", context)

def getmodel(request):
    size = request.GET.get('size', None)
    crust = request.GET.get('crust', None)
    print(type(size))
    if size == '2' and crust == '1':
        data = serializers.serialize('json', FlavourSSic.objects.all())
        return HttpResponse(data, content_type="application/json")
    if size == '1' and crust == '1':
        data = serializers.serialize('json', FlavourLSic.objects.all())
        return HttpResponse(data, content_type="application/json")

    if size == '2' and crust == '2':
        data = serializers.serialize('json', Flavour.objects.all())
        return HttpResponse(data, content_type="application/json")
    if size == '1' and crust == '2':
        data = serializers.serialize('json', FlavourLReg.objects.all())
        return HttpResponse(data, content_type="application/json")

        

def addpizza(request):
    if request.method == 'POST':
        print(request.POST)
        toppings = request.POST.getlist('topcheck')
        size = request.POST['size']
        crust = request.POST['crust']
        flavour = request.POST['flavmodel']
        print(toppings)
        print(size)
        print(crust)
        print(flavour)
        if size == '1' and crust == '1':
            newPizza = Pizza.objects.create(
                size = Size.objects.get(pk=size),
                crust = Crust.objects.get(pk=crust),
                flavourls = FlavourLSic.objects.get(pk=flavour)
            )
            for t in toppings:
                newPizza.toppings.add(Toppings.objects.get(pk=t))

        if size == '1' and crust == '2':
            newPizza = Pizza.objects.create(
                size = Size.objects.get(pk=size),
                crust = Crust.objects.get(pk=crust),
                flavourlr = FlavourLReg.objects.get(pk=flavour)
            )
            for t in toppings:
                newPizza.toppings.add(Toppings.objects.get(pk=t))

        if size == '2' and crust == '2':
            newPizza = Pizza.objects.create(
                size = Size.objects.get(pk=size),
                crust = Crust.objects.get(pk=crust),
                flavoursr = Flavour.objects.get(pk=flavour)
            )
            for t in toppings:
                newPizza.toppings.add(Toppings.objects.get(pk=t))

        if size == '2' and crust == '1':
            newPizza = Pizza.objects.create(
                size = Size.objects.get(pk=size),
                crust = Crust.objects.get(pk=crust),
                flavourss = FlavourSSic.objects.get(pk=flavour)
            )
            for t in toppings:
                newPizza.toppings.add(Toppings.objects.get(pk=t))


        newItem = Cart.objects.create(
            customer = request.user,
            pizza = Pizza.objects.get(pk=newPizza.id)
        )
    return HttpResponse('wtf', content_type="application/json")


def addsub(request):
    if request.method == 'POST':
        print(request.POST)
        sub = request.POST['sub']
        Cart.objects.filter(customer=request.user).update(sub=sub)
        #newItem.subs.add(Sub.objects.get(pk=sub))
        #toppings = request.POST.getlist('topcheck')
        # size = request.POST['size']


    return HttpResponse('wtf', content_type="application/json")