import unittest
from SeusPedidos.App.validation.pedido import PedidoValidation


class TesteValidacaoPedido(unittest.TestCase):

    validation = None

    def setUp(self):
        self.validation = PedidoValidation(None)
        self.validation.post = self.pegar_dados_padroes()
        self.validation.data = self.pegar_dados_padroes()

    def pegar_dados_padroes(self):
        dados = {
            'cliente_id': 1,
            'itens': {
                0: {
                    'quantidade': 2,
                    'desconto': 10,
                    'produto': {
                        'id': 1,
                        'nome': 'Produto Teste',
                        'valor': 120,
                    },
                },
            }
        }
        return dados

    def teste_form_valido_com_cliente_e_um_produto(self):
        result = self.validation.is_valid()
        self.assertEqual(result, True)

    def teste_form_valido_com_cliente_e_cinco_produtos(self):
        dados = self.pegar_dados_padroes()
        for i in range(2, 6):
            dados['itens'][i] = {
                'quantidade': 2,
                'desconto': i*3,
                'produto': {
                    'id': i,
                    'nome': 'Produto Teste #' + str(i),
                    'valor': 220 * i,
                },
            }

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, True)

    def teste_form_invalido_com_cliente_e_sem_produto(self):
        dados = self.pegar_dados_padroes()
        dados['itens'] = {}

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, False)

    def teste_form_invalido_sem_cliente_e_com_produto(self):
        dados = self.pegar_dados_padroes()
        dados['cliente_id'] = None

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, False)

    def teste_form_invalido_com_cliente_e_item_invalido_desconto_nao_informado(self):
        dados = self.pegar_dados_padroes()
        dados['itens'][0] = {
            'quantidade': 2,
            'produto': {
                'id': 1,
                'nome': 'Produto Teste',
                'valor': 220,
            },
        }

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, False)

    def teste_form_invalido_com_cliente_e_item_invalido_quantidade_nao_informada(self):
        dados = self.pegar_dados_padroes()
        dados['itens'][0] = {
            'desconto': 2,
            'produto': {
                'id': 1,
                'nome': 'Produto Teste',
                'valor': 220,
            },
        }

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, False)

    def teste_form_invalido_com_cliente_e_item_invalido_produto_nao_informado(self):
        dados = self.pegar_dados_padroes()
        dados['itens'][0] = {
            'desconto': 2,
            'quantidade': 2,
        }

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, False)

    def teste_form_invalido_com_cliente_e_um_item_valido_e_um_item_invalido(self):
        dados = self.pegar_dados_padroes()
        dados['itens'][1] = {
            'desconto': 2,
            'produto': {
                'id': 1,
                'nome': 'Produto Teste',
                'valor': 220,
            },
        }

        self.validation.data = dados
        self.validation.post = dados

        result = self.validation.is_valid()
        self.assertEqual(result, False)