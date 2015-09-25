import json

from django.http import HttpResponse
from django.core import serializers
from SeusPedidos.App.models.cliente import Cliente as ClienteModel
from SeusPedidos.App.models.pedido import Pedido as PedidoModel
from SeusPedidos.App.core.apiview import ApiView
from SeusPedidos.App.form.cliente import ClienteForm


class Cliente(ApiView):

    def get(self, request):
        id = request.GET.get('id')
        try:
            if not id:
                result = ClienteModel.objects.all()
            else:
                result = ClienteModel.objects.get(id=id)
        except ClienteModel.DoesNotExist:
            result = {}

        return HttpResponse(
            serializers.serialize('json', result), mimetype='application/json'
        )

    def post(self, request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            if (id == None):
                try:
                    cliente = ClienteModel.objects.create(
                        nome=request.POST.get('nome'),
                        email=request.POST.get('email')
                    )
                    if (cliente != None):
                        result = self._apiresult.success(None)
                    else:
                        result = self._apiresult.error(None)
                except Exception:
                    result = self._apiresult.error(None)
            else:
                try:
                    cliente = ClienteModel.objects.get(id=id)
                    cliente.nome = request.POST.get('nome', cliente.nome)
                    cliente.email = request.POST.get('email', cliente.email)
                    cliente.save()
                    result = self._apiresult.success(None)
                except Exception:
                    result = self._apiresult.error(None)
        else:
            result = self._apiresult.error(
                form.errors
            )

        return HttpResponse(
            json.dumps(result)
        )

    def delete(self, request):
        id = request.GET.get('id')
        total = PedidoModel.objects.filter(cliente=id).count()
        if (total == 0):
            try:
                cliente = ClienteModel.objects.get(id=id)
                cliente.delete()
                result = self._apiresult.success(None)
            except:
                result = self._apiresult.error(None)
        else:
            result = self._apiresult.error(None)
        return HttpResponse(
            json.dumps(result)
        )