import json

from django.http import HttpResponse
from django.core import serializers
from SeusPedidos.App.models.produto import Produto as ProdutoModel
from SeusPedidos.App.core.apiview import ApiView
from SeusPedidos.App.form.produto import ProdutoForm


class Produto(ApiView):

    def get(self, request):
        id = request.GET.get('id')
        try:
            if not id:
                result = ProdutoModel.objects.all()
            else:
                result = ProdutoModel.objects.get(id=id)
        except ProdutoModel.DoesNotExist:
            result = {}

        return HttpResponse(
            serializers.serialize('json', result)
        )

    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            if (id == None):
                try:
                    produto = ProdutoModel.objects.create(
                        nome=request.POST.get('nome'),
                        valor=request.POST.get('valor')
                    )
                    if (produto != None):
                        result = self._apiresult.success(None)
                    else:
                        result = self._apiresult.error(None)
                except Exception:
                    result = self._apiresult.error(None)
            else:
                try:
                    produto = ProdutoModel.objects.get(id=id)
                    produto.nome = request.POST.get('nome', produto.nome)
                    produto.valor = request.POST.get('valor', produto.valor)
                    produto.save()
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
        try:
            produto = ProdutoModel.objects.get(id=id)
            produto.delete()
            result = self._apiresult.success(None)
        except:
            result = self._apiresult.error(None)
        return HttpResponse(
            json.dumps(result)
        )
