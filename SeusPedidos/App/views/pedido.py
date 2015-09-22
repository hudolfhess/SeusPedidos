from django.shortcuts import render
from django.views.generic import View
from SeusPedidos.App.bo.pedidobo import PedidoBO
import json


class PedidoListar(View):
    def get(self, request):
        return render(request, 'App/pedido/index.html')


class PedidoForm(View):
    def get(self, request, id = None):
        data = {
            'editable': 0
        }
        if (id != None):
            #resultBO = PedidoBO()
            #pedido = resultBO.getById(id)
            data = {
                'editable': 1,
                'pedidoId': id
            }
        return render(request, 'App/pedido/form.html', data)