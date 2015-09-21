from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(min_length=1,max_length=100)
    valor = forms.DecimalField(min_value=0)