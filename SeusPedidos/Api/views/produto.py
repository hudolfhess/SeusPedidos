from django.http import HttpResponse
from django.views.generic import View
from SeusPedidos.App.models.produto import Produto as ProdutoModel
from django.core import serializers
import json

class Produto(View):
    def get(self, request):
        id = request.GET.get('id')
        try:
            if (id == None):
                data = ProdutoModel.objects.all()
                result = []
                if (data != None):
                    for row in data:
                        result.append(row)
            else:
                result = ProdutoModel.objects.get(id=id)
        except Exception:
            result = {}

        return HttpResponse(
            serializers.serialize('json', result)
        )

    def post(self, request):
        #@TODO FAZER VALIDACAO

        ProdutoModel.objects.create(
            nome=request.POST.get('nome'),
            valor=request.POST.get('valor')
        )

        return HttpResponse(
            'aaaa'
        )