from datetime import datetime
from SeusPedidos.App.models.pedido import Pedido as PedidoModel
from SeusPedidos.App.models.produto_pedido import Produto_Pedido as ProdutoPedidoModel
from SeusPedidos.App.models.produto import Produto as ProdutoModel
from SeusPedidos.App.models.cliente import Cliente as ClienteModel
from SeusPedidos.App.helpers.decimalencoder import DecimalEncoder


class PedidoBO:
    def insert(self, data):
        try:
            pedido = PedidoModel.objects.create(
                cliente_id=data['cliente_id'],
                status=1,
                data_hora=datetime.now()
            )
            if (pedido):
                for indexItem in data['itens']:
                    self.createProductRelations(pedido.id, data['itens'][indexItem])
                return True
        except Exception:
            return False

        return False

    def edit(self, id, data):
        try:
            pedido = PedidoModel.objects.get(id=id)
            if (pedido):
                if data.has_key('cliente_id'):
                    pedido.cliente_id = data['cliente_id']
                if data.has_key('status'):
                    pedido.status = data['status']
                if data.has_key('itens'):
                    self.removeProductRelations(pedido.id)
                    for indexItem in data['itens']:
                        self.createProductRelations(pedido.id, data['itens'][indexItem])
                    return True
        except Exception:
            return False
        return False

    def delete(self, id):
        try:
            pedido = PedidoModel.objects.get(id=id)
            if (pedido):
                self.removeProductRelations(id)
                pedido.delete()
                return True
        except Exception:
            return False
        return False

    def removeProductRelations(self, idPedido):
        produtosPedido = ProdutoPedidoModel.objects.filter(pedido=idPedido)
        for item in produtosPedido:
            item.delete()

    def createProductRelations(self, idPedido, itemData):
        ProdutoPedidoModel.objects.create(
            pedido_id=idPedido,
            produto_id=itemData['produto']['id'],
            valor_unidade=itemData['produto']['valor'],
            desconto=(float(itemData['desconto'])/100),
            quantidade=itemData['quantidade']
        )

    def getById(self, id):
        try:
            result = PedidoModel.objects.get(id=id)
            return self.prepareResult(result)
        except Exception:
            return {}

    def getList(self):
        try:
            data = PedidoModel.objects.all().values()
            if (data):
                result = []
                for row in data:
                    result.append(self.prepareResult(row))
            return result
        except Exception:
            return {}

    def prepareResult(self, row):
        if isinstance(row, PedidoModel):
            obj = row
            row = {
                'id': obj.id,
                'cliente_id': obj.cliente_id,
                'status': obj.status,
                'data_hora': obj.data_hora,
            }

        cliente = ClienteModel.objects.get(id=row['cliente_id'])
        itens = ProdutoPedidoModel.objects.filter(pedido=row['id'])

        row['total'] = 0
        row['itens'] = []
        row['cliente'] = {
            'id': cliente.nome,
            'nome': cliente.nome
        }

        for item in itens:
            produto = ProdutoModel.objects.get(id=item.produto_id)
            row['itens'].append({
                'id': item.id,
                'produto': {
                    'id': produto.id,
                    'nome': produto.nome,
                    'valor': DecimalEncoder.encode(produto.valor)
                },
                'quantidade': item.quantidade,
                'desconto': int(item.desconto * 100),
                'valor_unidade': DecimalEncoder.encode(item.valor_unidade)
            })
            row['total'] += ((item.valor_unidade * (1 - item.desconto)) * item.quantidade)

        row['total'] = DecimalEncoder.encode(row['total'])
        row['data_hora'] = row['data_hora'].strftime('%d/%m/%Y %H:%M:%S')
        row['status_description'] = 'Em aberto'
        if (row['status'] == 2):
            row['status'] = 'Fechado/E-mail enviado'
        else:
            if (row['status'] == 3):
                row['status'] = 'Cancelado'

        return row