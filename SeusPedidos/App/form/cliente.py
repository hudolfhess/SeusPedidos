from django import forms

class ClienteForm(forms.Form):
    nome = forms.CharField(min_length=1,max_length=100)
    email = forms.EmailField()