from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Toppings(models.Model): 
    topping = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.topping}"

class Crust(models.Model):
    crust = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"{self.crust}"

class Size(models.Model):
    size = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"{self.size}"

class Flavour(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #fields.GenericRelation(Pizza)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class FlavourLReg(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #fields.GenericRelation(Pizza)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class FlavourLSic(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #fields.GenericRelation(Pizza)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class FlavourSSic(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #fields.GenericRelation(Pizza)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete = models.CASCADE, related_name="pizzasize")
    crust = models.ForeignKey(Crust, on_delete = models.CASCADE, related_name="pizzacrust")
    flavoursr = models.ForeignKey(Flavour, null=True, blank=True, on_delete = models.CASCADE, related_name="fsr")
    flavourlr = models.ForeignKey(FlavourLReg, null=True, blank=True, on_delete = models.CASCADE, related_name="flr")
    flavourss = models.ForeignKey(FlavourSSic, null=True, blank=True, on_delete = models.CASCADE, related_name="fss")
    flavourls = models.ForeignKey(FlavourLSic, null=True, blank=True, on_delete = models.CASCADE, related_name="fls")
    toppings = models.ManyToManyField(Toppings, blank=True, related_name="pizzatoppings")

    @property
    def owner(self):
        if self.flavoursr_id is not None:
            return self.flavoursr
        if self.flavourlr_id is not None:
            return self.flavourlr
        if self.flavourss_id is not None:
            return self.flavourss
        if self.flavourls_id is not None:
            return self.flavourls
        raise AssertionError("Pizza Type is not set")
    
    def __str__(self):
        return f"{self.size} {self.crust} {self.owner} {self.toppings}"

class SteakCheeseExtras(models.Model): 
    scextras = models.CharField(max_length = 64)
    price = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.scextras} {self.price}"

class ExtraCheese(models.Model):
    extra = models.BooleanField(default=False)
    price = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.extra} {self.price}"

class Sub(models.Model):
    flavour = models.CharField(max_length = 64)
    size = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.flavour} {self.size} {self.price}"

class SubOrder(models.Model):
    sub = models.ForeignKey(Sub, on_delete = models.CASCADE, related_name="basesub")
    extracheese = models.ForeignKey(ExtraCheese, null=True, blank=True, on_delete = models.CASCADE, related_name="extracheese")
    extratoppings = models.ManyToManyField(SteakCheeseExtras, blank=True, related_name="extratoppings")
    
    def __str__(self):
        return f"{self.sub} {self.extracheese} {self.extratoppings}"

class Pasta(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class Salad(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class DinnerPlatter(models.Model):
    flavour = models.CharField(max_length = 64)
    size = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.flavour} {self.size} {self.price}"

class PastaOrder(models.Model):
    pasta = models.ForeignKey(Pasta, on_delete = models.CASCADE, related_name="pastaorder")
    
    def __str__(self):
        return f"{self.pasta}"

class SaladOrder(models.Model):
    salad = models.ForeignKey(Salad, on_delete = models.CASCADE, related_name="saldorder")
    
    def __str__(self):
        return f"{self.salad}"

class DinnerPlatterOrder(models.Model):
    dinnerplatter = models.ForeignKey(DinnerPlatter, on_delete = models.CASCADE, related_name="platterorder")
    
    def __str__(self):
        return f"{self.dinnerplatter}"

class Cart(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, null=True, blank=True, on_delete = models.CASCADE)
    sub = models.ForeignKey(SubOrder, null=True, blank=True, on_delete = models.CASCADE)
    pasta = models.ForeignKey(PastaOrder, null=True, blank=True, on_delete = models.CASCADE)
    salad = models.ForeignKey(SaladOrder, null=True, blank=True, on_delete = models.CASCADE)
    dinnerplatter = models.ForeignKey(DinnerPlatterOrder, null=True, blank=True, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.customer} {self.pizza} {self.sub} {self.pasta} {self.salad} {self.dinnerplatter}"