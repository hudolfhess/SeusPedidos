from django.views.generic import View
from SeusPedidos.App.core.apiresult import ApiResult

class ApiView(View):

    _apiresult = None

    def __init__(self):
        self._apiresult = ApiResult()