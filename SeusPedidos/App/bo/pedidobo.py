from SeusPedidos.App.models.pedido import Pedido as PedidoModel
from SeusPedidos.App.models.produto_pedido import Produto_Pedido as ProdutoPedidoModel
from SeusPedidos.App.models.produto import Produto as ProdutoModel
from SeusPedidos.App.models.cliente import Cliente as ClienteModel
from SeusPedidos.App.helpers.decimalencoder import DecimalEncoder


class PedidoBO:
    def insert(self, data):
        return ''

    def getById(self, id):
        try:
            result = PedidoModel.objects.all(id=id)
            return self.prepareResult(result)
        except Exception:
            return {}

    def getList(self):
        #try:
        data = PedidoModel.objects.all().values()
        if (data):
            result = []
            for row in data:
                result.append(self.prepareResult(row))
        return result
        #except Exception:
        #    return {}

    def prepareResult(self, row):
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
                'desconto': DecimalEncoder.encode(item.desconto) * 100,
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