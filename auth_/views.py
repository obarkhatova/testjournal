from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


from .serializers import LoginSerializer
from core.authentication import enforsed_csrf_disabled


@enforsed_csrf_disabled
class AuthViewSet(ViewSet):
    permission_classes = ()

    serializer_class = LoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is None:
            return Response({"detail": "invalid username or password"},
                            status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response()

    @action(detail=False,
            methods=['get', 'post'],
            serializer_class=None)
    def logout(self, request):
        logout(request)
        return Response()
