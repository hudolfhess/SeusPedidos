from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from SeusPedidos.App.core.auth import Auth

class Index(View):
    def get(self, request):
        return render(request, 'App/index/index.html')

    def post(self, request):
        postData = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        authObj = Auth()
        if (authObj.isValid(postData)):
            return HttpResponse("Aeee caraiii, foi...")
        else:
            return HttpResponse("Usuario e/ou senha nao conferem.")