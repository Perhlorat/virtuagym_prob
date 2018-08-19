from datetime import datetime

import pytz
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView


class ObtainAuthTokenView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        token, created = Token.objects.get_or_create(user=user)
        if token.created < utc_now - settings.TOKEN_EXPIRE_TIME:
            token.delete()
            token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class RefreshAuthTokenView(APIView):
    """
    View to refresh token if it is valid to refresh

    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        try:
            token = Token.objects.get(key=token)
        except Exception:
            raise exceptions.AuthenticationFailed('Invalid token')
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if token.created < utc_now - settings.TOKEN_EXPIRE_TIME:
            token.delete()

        if token.created < utc_now - settings.TOKEN_EXPIRE_TIME - settings.TOKEN_REFRESH_TIME:
            raise exceptions.AuthenticationFailed('Token is too old')

        new_token, created = Token.objects.get_or_create(user=token.user)
        return Response({'token': new_token.key})
