import json

from django.http import HttpResponse
from django.core import serializers
from datetime import datetime
from SeusPedidos.App.bo.pedidobo import PedidoBO
from SeusPedidos.App.models.pedido import Pedido as PedidoModel
from SeusPedidos.App.models.produto_pedido import Produto_Pedido as ProdutoPedidoModel
from SeusPedidos.App.core.apiview import ApiView
from SeusPedidos.App.form.pedido import PedidoForm
from SeusPedidos.App.core import parser


class Pedido(ApiView):

    def get(self, request):
        id = request.GET.get('id')
        #try:
        bo = PedidoBO()
        if (id == None):
            result = bo.getList()
        else:
            result = bo.getById(id)
        #except Exception:
        #    result = {''}

        return HttpResponse(
            json.dumps(result)
        )

    def post(self, request):
        form = PedidoForm(request.POST)
        if (form.is_valid() == True):
            id = request.POST.get('id')
            if (id == None):
                try:
                    pedido = PedidoModel.objects.create(
                        cliente_id=request.POST.get('cliente_id'),
                        status=1,
                        data_hora=datetime.now()
                    )
                    if (pedido):
                        postData = parser.parse(request.POST.urlencode())
                        for indexItem in postData['itens']:
                            ProdutoPedidoModel.objects.create(
                                pedido_id=pedido.id,
                                produto_id=postData['itens'][indexItem]['produto']['id'],
                                valor_unidade=postData['itens'][indexItem]['produto']['valor'],
                                desconto=(float(postData['itens'][indexItem]['desconto'])/100),
                                quantidade=postData['itens'][indexItem]['quantidade']
                            )
                        result = self._apiresult.success(None)
                    else:
                        result = self._apiresult.error(None)
                except Exception:
                    result = self._apiresult.error(None)
            else:
                result = self._apiresult.error(None)
        else:
            print form.is_valid()
            result = self._apiresult.error(
                form.errors
            )

        return HttpResponse(
            json.dumps(result)
        )
