from django.conf.urls.defaults import patterns, include, url

# WEB APP IMPORTS
import SeusPedidos
from SeusPedidos.App.views.index import Index
from SeusPedidos.App.views.cliente import Cliente
from SeusPedidos.App.views.produto import Produto
from SeusPedidos.App.views.pedido import PedidoForm, PedidoListar

# API IMPORTS
from SeusPedidos.Api.views.produto import Produto as ApiProduto
from SeusPedidos.Api.views.cliente import Cliente as ApiCliente
from SeusPedidos.Api.views.pedido import Pedido as ApiPedido

urlpatterns = patterns(
    '',
    # WEB APP URLS
    url(r'^$', Index.as_view()),
    url(r'^cliente/?$', Cliente.as_view()),
    url(r'^produto/?$', Produto.as_view()),
    url(r'^pedido/?$', PedidoListar.as_view()),
    url(r'^pedido/cadastrar/?$', PedidoForm.as_view()),
    url(r'^pedido/alterar/([0-9]{1,11})/?$', PedidoForm.as_view()),

    # API URLS
    url(r'^api/produto/?$', ApiProduto.as_view()),
    url(r'^api/cliente/?', ApiCliente.as_view()),
    url(r'^api/pedido/?', ApiPedido.as_view()),
)