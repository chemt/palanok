from django import forms

class PayForm(forms.Form):
    name  = forms.CharField(200, required=True)
    email = forms.EmailField(200, required=False)
    tel   = forms.CharField(200, required=False)
