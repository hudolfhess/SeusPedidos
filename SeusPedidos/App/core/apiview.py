from django.views.generic import View
from SeusPedidos.App.core.apiviewresult import ApiViewResult
from SeusPedidos.App.core import parser
import json


class ApiView(View):
    _apiresult = None

    _postData = None

    def __init__(self):
        self._apiresult = ApiViewResult()

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            raw_data = request.raw_post_data.replace('\'', '"')
            if request.raw_post_data != '' and request.environ["CONTENT_TYPE"] == 'application/json':
                self._postData = json.loads(raw_data)
        return super(ApiView, self).dispatch(request, *args, **kwargs)
