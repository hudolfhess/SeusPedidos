import json

from django.http import HttpResponse
from SeusPedidos.App.bo.pedidobo import PedidoBO
from SeusPedidos.App.core.apiview import ApiView
from SeusPedidos.App.core import parser
from SeusPedidos.App.validation.pedido import PedidoValidation
from SeusPedidos.App.models.pedido import Pedido as PedidoModel
from SeusPedidos.App.models.cliente import Cliente as ClienteModel
from SeusPedidos.App.celery.send_email import send_email


class Pedido(ApiView):

    resultBO = None

    def __init__(self):
        super(Pedido, self).__init__()
        self.resultBO = PedidoBO()

    def get(self, request):
        id = request.GET.get('id')
        try:
            if (id == None):
                result = self.resultBO.getList()
            else:
                result = self.resultBO.getById(id)
        except Exception:
            result = {}

        return HttpResponse(
            json.dumps(result), mimetype='application/json'
        )

    def post(self, request):
        validation = PedidoValidation(self._postData)
        if (validation.is_valid() == True):
            id = self._postData.get('id')
            if (id == None):
                if self.resultBO.insert(self._postData):
                    result = self._apiresult.success(None)
                else:
                    result = self._apiresult.error(None)
            else:
                if self.resultBO.edit(self._postData.get('id'), self._postData):
                    result = self._apiresult.success(None)
                else:
                    result = self._apiresult.error(None)
        else:
            result = self._apiresult.error(
                validation.errors
            )

        return HttpResponse(
            json.dumps(result), mimetype='application/json'
        )

    def delete(self, request):
        id = request.GET.get('id')
        if (id != None):
            if (self.resultBO.delete(id) == True):
                result = self._apiresult.success(None)
            else:
                result = self._apiresult.error(None)
        else:
            result = self._apiresult.error(None)
        return HttpResponse(
            json.dumps(result), mimetype='application/json'
        )


class PedidoEmail(ApiView):
    def post(self, request):
        id = request.POST.get('id')
        try:
            if (id != None):
                pedido = PedidoModel.objects.get(id=id)
                if (pedido):
                    cliente = ClienteModel.objects.get(id=pedido.cliente_id)
                    send_email.delay(
                        'Dados do pedido #' + str(pedido.id),
                        'Confira abaixo os detalhes do pedido #' + str(pedido.id),
                        cliente.email
                    )
                    pedido.status = 2
                    pedido.save()
                    result = self._apiresult.success(None)
                else:
                    result = self._apiresult.error(None)
            else:
                result = self._apiresult.error(None)
        except Exception:
            result = self._apiresult.error(None)
        return HttpResponse(
            json.dumps(result), mimetype='application/json'
        )