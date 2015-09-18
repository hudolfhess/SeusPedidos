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
                result = ProdutoModel.objects.all()
                #result = []
                #if (data != None):
                #    for x in range(0, len(data)):
                #        result.append(data[x])
            else:
                result = ProdutoModel.objects.get(id=id)
        except Exception:
            result = {}

        return HttpResponse(
            serializers.serialize('json', result)
        )

    def post(self, request):
        #@TODO FAZER VALIDACAO

        #try:
        produto = ProdutoModel.objects.create(
            nome=request.POST.get('nome'),
            valor=request.POST.get('valor')
        )
        if (produto != None):
            result = {
                'success': 1
            }
        else:
            result = {
                'success': 0
            }
        #except Exception:
        #    result = {
        #        'success': 0
        #    }

        return HttpResponse(
            json.dumps(result)
        )