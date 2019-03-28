from django.db import models

# Create your models here.

class Toppings(models.Model): 
    topping = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.topping}"

class Crust(models.Model):
    crust = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.crust} {self.price}"

class Size(models.Model):
    size = models.CharField(max_length = 64)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.size} {self.price}"

class Flavour(models.Model):
    flavour = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.flavour} {self.price}"

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete = models.CASCADE, related_name="pizzasize")
    crust = models.ForeignKey(Crust, on_delete = models.CASCADE, related_name="pizzacrust")
    flavour = models.ForeignKey(Flavour, on_delete = models.CASCADE, related_name="pizzaflavour")
    toppings = models.ManyToManyField(Toppings, blank=True, related_name="pizzatoppings")
    
    def __str__(self):
        return f"{self.size} {self.crust} {self.flavour} {self.toppings}"