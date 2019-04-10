from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages

from .models import *

def index(request):
    context = {
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
        "pasta": Pasta.objects.all(),
        "salad": Salad.objects.all(),
        "dinnerplatter": DinnerPlatter.objects.all(),
        }

    return render(request, "orders/index.html", context)

def checkout(request):
    context = {}
    if Cart.objects.filter(customer=request.user).exists():
        cartcontents = Cart.objects.get(customer=request.user)
        print (cartcontents)
        sumofet = 0
        
        if cartcontents.sub and cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.sub.sub.price + cartcontents.sub.extracheese.price + sumofet + cartcontents.pizza.owner.price

        if cartcontents.sub and not cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.sub.sub.price + cartcontents.sub.extracheese.price + sumofet

        if cartcontents.pizza and not cartcontents.sub:
            totalprice = cartcontents.pizza.owner.price

        if cartcontents.pasta and not cartcontents.sub and not cartcontents.pizza:
            totalprice = cartcontents.pasta.pasta.price

        if cartcontents.pasta and cartcontents.sub and not cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.pasta.pasta.price + cartcontents.sub.sub.price + cartcontents.sub.extracheese.price + sumofet

        if cartcontents.pasta and cartcontents.sub and cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.pasta.pasta.price + cartcontents.sub.sub.price + cartcontents.sub.extracheese.price + sumofet + cartcontents.pizza.owner.price

        if cartcontents.pasta and not cartcontents.sub and cartcontents.pizza:
            totalprice = cartcontents.pasta.pasta.price + cartcontents.pizza.owner.price

        if cartcontents.salad and not cartcontents.pasta and not cartcontents.sub and not cartcontents.pizza:
            totalprice = cartcontents.salad.salad.price

        if cartcontents.salad and cartcontents.pasta and not cartcontents.sub and not cartcontents.pizza:
            totalprice = cartcontents.salad.salad.price + cartcontents.pasta.pasta.price

        if cartcontents.salad and cartcontents.pasta and cartcontents.sub and not cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.salad.salad.price + cartcontents.pasta.pasta.price + sumofet + cartcontents.sub.extracheese.price + cartcontents.sub.sub.price

        if cartcontents.salad and cartcontents.pasta and cartcontents.sub and cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.salad.salad.price + cartcontents.pasta.pasta.price + cartcontents.sub.sub.price + cartcontents.sub.extracheese.price + sumofet + cartcontents.pizza.owner.price

        if cartcontents.salad and not cartcontents.pasta and not cartcontents.sub and cartcontents.pizza:
            totalprice = cartcontents.salad.salad.price + cartcontents.pizza.owner.price

        if cartcontents.salad and not cartcontents.pasta and cartcontents.sub and not cartcontents.pizza:
            for t in cartcontents.sub.extratoppings.all():
                sumofet =+ t.price
            totalprice = cartcontents.salad.salad.price  + sumofet + cartcontents.sub.extracheese.price + cartcontents.sub.sub.price

        
        context = {
            "cartcontents": cartcontents,
            "totalprice": totalprice,
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
        toppings = request.POST.getlist('topcheck')
        size = request.POST['size']
        crust = request.POST['crust']
        flavour = request.POST['flavmodel']

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
            messages.success(request, f'Pizza Added.')
        else:
            newItem = Cart.objects.create(
            customer = request.user,
            pizza = Pizza.objects.get(pk=newPizza.id)
            )
            messages.success(request, f'Pizza Added.')
    
    return redirect('index')


def addsub(request):
    if request.method == 'POST':
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

    return redirect('index')

def addpasta(request):
    if request.method == 'POST':
        print(request.POST)
        pasta = request.POST['pasta']
        newPasta= PastaOrder.objects.create(
                pasta = Pasta.objects.get(pk=pasta)
            )
        # if a cart exists for the current user update cart, else create new cart
        if Cart.objects.filter(customer=request.user).exists():
            Cart.objects.filter(customer=request.user).update(pasta=newPasta)
            messages.success(request, f'Pasta Added.')
            
        else:
            newItem = Cart.objects.create(
            customer = request.user,
            pasta = PastaOrder.objects.get(pk=newPasta.id)
            )
            messages.success(request, f'Pasta Added.')

    return redirect('index')

def addsalad(request):
    if request.method == 'POST':
        print(request.POST)
        salad = request.POST['salad']
        newSalad= SaladOrder.objects.create(
                salad = Salad.objects.get(pk=salad)
            )
        # if a cart exists for the current user update cart, else create new cart
        if Cart.objects.filter(customer=request.user).exists():
            Cart.objects.filter(customer=request.user).update(salad=newSalad)
            messages.success(request, f'Salad Added.')
            
        else:
            newItem = Cart.objects.create(
            customer = request.user,
            salad = SaladOrder.objects.get(pk=newSalad.id)
            )
            messages.success(request, f'Salad Added.')

    return redirect('index')

def addplatter(request):
    if request.method == 'POST':
        print(request.POST)
        platter = request.POST['platter']
        newPlatter= DinnerPlatterOrder.objects.create(
                dinnerplatter = DinnerPlatter.objects.get(pk=platter)
            )
        # if a cart exists for the current user update cart, else create new cart
        if Cart.objects.filter(customer=request.user).exists():
            Cart.objects.filter(customer=request.user).update(dinnerplatter=newPlatter)
            messages.success(request, f'Platter Added.')
            
        else:
            newItem = Cart.objects.create(
            customer = request.user,
            dinnerplatter = DinnerPlatterOrder.objects.get(pk=newPlatter.id)
            )
            messages.success(request, f'Platter Added.')

    return redirect('index')