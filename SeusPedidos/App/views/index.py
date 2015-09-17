from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

'''
def ini(request):
    return HttpResponse("Hello World")

'''

class index(View):
    def get(self, request):
        return render(request, 'App/index/index.html')
        #return HttpResponse("Get: Hello World!!!")