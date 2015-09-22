from django.views.generic import View
from django.http import HttpResponseRedirect


class Index(View):
    def get(self, request):
        return HttpResponseRedirect('/pedido')
