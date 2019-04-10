from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
#from .forms import LargeSicilian, SmallSicilian
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages



from .models import Pizza, Toppings, Crust, Size, Flavour, FlavourLReg, FlavourLSic, FlavourSSic, Cart, Sub, SteakCheeseExtras, ExtraCheese, SubOrder

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
        "subs": Sub.objects.all(),
        "scextras": SteakCheeseExtras.objects.all(),
        "extracheese": ExtraCheese.objects.all(),
        "suborder": SubOrder.objects.all()

    }
    return render(request, "orders/index.html", context)

def checkout(request):
    cartcontents = Cart.objects.get(customer=request.user)
    print (cartcontents)
    #pizza = Pizza.objects.get(pk=2)
    #fl = FlavourLSic.objects.all()
    #fls = json.dumps(list(fl), cls=DjangoJSONEncoder)
    #fls = json.dumps(fl)
    #ccser = serializers.serialize('json', cartcontents)
    #print(ccser)
    #form = SmallSicilian()
    context = {
        "cartcontents": cartcontents,
        "customer": cartcontents.customer,
        "sub": cartcontents.sub.sub.flavour,
        "subsize": cartcontents.sub.sub.size,
        "subprice": cartcontents.sub.sub.price,
        "extracheese": cartcontents.sub.extracheese.extra,
        "extracheeseprice": cartcontents.sub.extracheese.price,
        "extratoppings": cartcontents.sub.extratoppings.all(),
        "extratoppingsprice": cartcontents.sub.extracheese.price,

    }
    
    return render(request, "orders/checkout.html", context)

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


        if Cart.objects.filter(customer=request.user).exists():
            Cart.objects.filter(customer=request.user).update(pizza=newPizza)
        else:
            newItem = Cart.objects.create(
            customer = request.user,
            pizza = Pizza.objects.get(pk=newPizza.id)
        )
        
    return HttpResponse('wtf', content_type="application/json")


def addsub(request):
    if request.method == 'POST':
        print(request.POST)
        sub = request.POST['sub']
        sccheck = request.POST.getlist('sccheck')
        extracheese = request.POST['extracheese']
        newSub = SubOrder.objects.create(
                sub = Sub.objects.get(pk=sub),
                extracheese = ExtraCheese.objects.get(pk=extracheese),
            )
        for t in sccheck:
            newSub.extratoppings.add(SteakCheeseExtras.objects.get(pk=t))

        if Cart.objects.filter(customer=request.user).exists():
            Cart.objects.filter(customer=request.user).update(sub=newSub)
            messages.success(request, f'Sub Added.')
            
        else:
            newItem = Cart.objects.create(
            customer = request.user,
            sub = SubOrder.objects.get(pk=newSub.id)
            )
            messages.success(request, f'Sub Added.')

        #newItem.subs.add(Sub.objects.get(pk=sub))
        #toppings = request.POST.getlist('topcheck')
        # size = request.POST['size']
        # 
    return redirect('index')