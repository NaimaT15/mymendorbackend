from django import forms
from django.forms import ModelForm
from .models import Feedback
class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback

        fields = ("title","description",)
        widgets = {
            "price": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "description"}
            ),
            
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
      
        }