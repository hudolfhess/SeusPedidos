from django import forms

class PedidoForm(forms.Form):
    cliente_id = forms.CharField()