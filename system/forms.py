from .models import Transaction_history,Customer

from django import forms

class customerbalanceform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('balance',)