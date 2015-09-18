from django.http import HttpResponse
from django.views.generic import View
import json

class Login(View):
    def post(self, request):
        return 'a'
        '''
        authObj = Auth()
        postData = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }

        if (authObj.isValid(postData) == True):
            result = {
                'success': 1,
                'authToken': 'AuthToken',
            }
        else:
            result = {
                'success': 0,
                'message': 'Usuario e/ou senha estao incorretos.'
            }
        return HttpResponse(
            json.dumps(result)
        )'''