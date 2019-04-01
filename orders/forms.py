from django import forms
from .models import Pizza, Toppings, Crust, Size, Flavour, FlavourLReg, FlavourLSic, FlavourSSic   
class SignupForm(forms.Form):
 #django gives a number of predefined fields
 #CharField and EmailField are only two of them
 #go through the official docs for more field details
    
    selectwidget = forms.ModelChoiceField(queryset=FlavourLSic.objects.all())
    
