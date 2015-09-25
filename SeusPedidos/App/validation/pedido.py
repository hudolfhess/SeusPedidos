from SeusPedidos.App.form.pedido import PedidoForm
from SeusPedidos.App.core import parser
import json


class PedidoValidation:
    data = {}
    post = None
    errors = {}

    def __init__(self, request):
        if (request != None):
            self.post = request.POST
            self.data = parser.parse(request.POST.urlencode())

    def is_valid(self):
        form = PedidoForm(self.post)
        errors = {
            'itens': '',
            'form': None
        }
        isValid = True
        if (form.is_valid()):
            if self.data.has_key('itens') and len(self.data['itens']) > 0:
                for indexItem in self.data['itens']:
                    item = self.data['itens'][indexItem]
                    if item.has_key('quantidade') == False or int(item['quantidade']) <= 0:
                        isValid = False
                        errors['itens'] = 'Item invalido'
                    elif item.has_key('desconto') == False or (int(item['desconto']) < 0 and int(item['desconto']) >= 100):
                        isValid = False
                        errors['itens'] = 'Item invalido'
                    elif item.has_key('produto') == False:
                        isValid = False
                        errors['itens'] = 'Item invalido'
                    else:
                        if item['produto'].has_key('id') == False or item['produto'].has_key('valor') == False:
                            isValid = False
                            errors['itens'] = 'Item invalido'
            else:
                isValid = False
                errors['itens'] = 'Necessario ao menos um item no pedido'
        else:
            isValid = False
            errors['form'] = form.errors
        self.errors = errors
        return isValid
