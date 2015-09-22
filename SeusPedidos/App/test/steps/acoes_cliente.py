from SeusPedidos.App.test.paginas.pagina_cliente import PaginaCliente

__author__ = 'hcassus'

class AcoesCliente:

    def __init__(self, driver):
        self.pagina = PaginaCliente(driver)

    def acessar_pagina(self):
        self.pagina.acessar()
        return self

    def cadastrar_cliente(self,nome,email):
        self.pagina.preencher_nome(nome)
        self.pagina.preencher_email(email)
        self.pagina.clicar_adicionar()

        self.nome_cliente = nome
        self.email_cliente = email
        return self

    def contar_clientes(self):
        self.contagem = self.pagina.contar_clientes()
        return self

    def verificar_mensagem_sucesso(self):
        assert 'Dados salvos com sucesso!' in self.pagina.obter_texto_alerta()
        return self

    def verificar_diferenca_numero_clientes(self,numero):
        assert self.pagina.contar_clientes() == self.contagem + numero
        return self

    def validar_ultimo_cliente(self):
        assert self.nome_cliente == self.pagina.obter_nome_ultimo_cliente()
        assert self.email_cliente == self.pagina.obter_email_ultimo_cliente()
        return self

    def remover_ultimo_cliente(self):
        self.pagina.remover_ultimo_cliente()
        return self