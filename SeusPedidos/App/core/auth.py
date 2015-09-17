from importlib import import_module
from django.conf import settings
from SeusPedidos.App.models.user import User

import hashlib

class Auth:
    def isValid(self, data):
        try:
            result = User.objects.get(
                username=data['username'],
                password=hashlib.sha1(data['password']).hexdigest()
            )
            if (result != None):
                SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
                sessionStore = SessionStore()
                sessionStore['uid'] = result.id
                sessionStore['username'] = result.username
                sessionStore.save()
                return True
        except Exception:
            result = None

        return False