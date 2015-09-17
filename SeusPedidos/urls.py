from django.conf.urls.defaults import patterns, include, url

# WEB APP IMPORTS
import SeusPedidos
from SeusPedidos.App.views.index import *
from SeusPedidos.App.views.cliente import *
from SeusPedidos.App.views.produto import *

# API IMPORTS
from SeusPedidos.Api.views.login import *
from SeusPedidos.Api.views.produto import Produto as ApiProduto

urlpatterns = patterns(
    '',
    # WEB APP URLS
    url(r'^$', Index.as_view()),
    url(r'^cliente$', Cliente.as_view()),
    url(r'^produto$', Produto.as_view()),

    # API URLS
    url(r'^api/login$', Login.as_view()),
    url(r'^api/produto$', ApiProduto.as_view()),
)