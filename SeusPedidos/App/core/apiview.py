from django.views.generic import View
from SeusPedidos.App.core.apiviewresult import ApiViewResult


class ApiView(View):

    _apiresult = None

    def __init__(self):
        self._apiresult = ApiViewResult()