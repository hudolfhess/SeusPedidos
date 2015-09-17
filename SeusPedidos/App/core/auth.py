from SeusPedidos.App.models.user import User
import hashlib

class Auth:
    def isValid(self, data):
        #userModel = User()
        #User.objects.create(name='Hudolf', username='hudolfhess', password=hashlib.sha1('testes123').hexdigest())

        try:
            result = User.objects.get(
                username=data['username'],
                password=hashlib.sha1(data['password']).hexdigest()
            )
            if (result != None):
                #CREATE SESSION DATA
                return True
        except Exception:
            result = None

        return False