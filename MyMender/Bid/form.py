from django import forms
from django.forms import ModelForm
from .models import Bid
class BidForm(ModelForm):
    class Meta:
        model = Bid

        fields = ("price","title",)
        widgets = {
            "price": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Price"}
            ),
            
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
      
        }
    