from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.settings import api_settings


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        pass


def enforsed_csrf_disabled(cls):
    auth_cls = list(api_settings.DEFAULT_AUTHENTICATION_CLASSES)
    if auth_cls.count(SessionAuthentication) == 0:
        return cls

    auth_cls[auth_cls.index(SessionAuthentication)] = CsrfExemptSessionAuthentication
    cls.authenticalion_classes = tuple(auth_cls)
    return cls



