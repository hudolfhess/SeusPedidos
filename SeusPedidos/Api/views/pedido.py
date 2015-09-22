import json

from django.http import HttpResponse
from SeusPedidos.App.bo.pedidobo import PedidoBO
from SeusPedidos.App.core.apiview import ApiView
from SeusPedidos.App.core import parser
from SeusPedidos.App.validation.pedido import PedidoValidation


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
            json.dumps(result)
        )

    def post(self, request):
        validation = PedidoValidation(request.POST)
        if (validation.is_valid() == True):
            id = request.POST.get('id')
            if (id == None):
                data = parser.parse(request.POST.urlencode())
                if self.resultBO.insert(data):
                    result = self._apiresult.success(None)
                else:
                    result = self._apiresult.error(None)
            else:
                data = parser.parse(request.POST.urlencode())
                if self.resultBO.edit(data['id'], data):
                    result = self._apiresult.success(None)
                else:
                    result = self._apiresult.error(None)
        else:
            result = self._apiresult.error(
                validation.errors
            )

        return HttpResponse(
            json.dumps(result)
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
            json.dumps(result)
        )