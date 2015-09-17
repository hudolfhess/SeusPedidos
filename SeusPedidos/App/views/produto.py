from django.shortcuts import render
from django.views.generic import View

class Produto(View):
    def get(self, request):
        return render(request, 'App/produto/index.html')