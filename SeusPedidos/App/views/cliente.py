from django.shortcuts import render
from django.views.generic import View

class Cliente(View):
    def get(self, request):
        return render(request, 'App/cliente/cliente.html')