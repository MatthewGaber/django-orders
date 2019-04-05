from django import forms
from .models import Pizza, Toppings, Crust, Size, Flavour, FlavourLReg, FlavourLSic, FlavourSSic   
class LargeSicilian(forms.Form):
    selectwidget = forms.ModelChoiceField(queryset=FlavourLSic.objects.all())

class SmallSicilian(forms.Form):
    selectwidget = forms.ModelChoiceField(queryset=FlavourSSic.objects.all())
    
