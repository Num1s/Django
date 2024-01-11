from django import forms
from . import models


class OrderCloth(forms.ModelForm):
    class Meta:
        model = models.OrderCloth
        fields = '__all__'