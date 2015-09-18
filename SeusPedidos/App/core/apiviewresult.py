import json

class ApiViewResult:
    def success(self, data):
        result = {
            'success': 1
        }
        if (data != None):
            result.data = data
        return result

    def error(self, error):
        result = {
            'success': 0
        }
        if (error != None):
            result.error = error
        return result

    def parseToJson(self, result):
        return json.dumps(result)