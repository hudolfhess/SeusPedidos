from django.shortcuts import render
from django.views.generic import View


class PedidoListar(View):
    def get(self, request):
        return render(request, 'App/pedido/index.html')


class PedidoForm(View):
    def get(self, request):
        return render(request, 'App/pedido/form.html')