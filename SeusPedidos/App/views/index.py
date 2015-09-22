from django.views.generic import View
from django.http import HttpResponseRedirect
from SeusPedidos.App.views.tasks import *


class Index(View):
    def get(self, request):
        send_email.delay(5)
        return HttpResponseRedirect('/pedido')
