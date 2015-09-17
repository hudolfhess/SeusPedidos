from django.http import HttpResponse
from SeusPedidos.App.core.auth import Auth
from django.views.generic import View

class Login(View):
    def post(self, request):
        authObj = Auth()
        postData = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        if (authObj.isValid(postData) == True):
            return HttpResponse("{success: 1, authToken: 'tokenauth'}")
        else:
            return HttpResponse("{success: 0, message: 'Usuario e/ou senha nao conferem.'}")