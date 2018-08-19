from django.utils.translation import gettext as _

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from plans.models import Plan
from plans.serializers import PlanSerializer


class PlanViewset(viewsets.ModelViewSet):
    """
    Simple restaurant REST API CRUD ViewSet
    """
    serializer_class = PlanSerializer
    queryset = Plan.objects.prefetch_related('users').all()

    @detail_route(methods=['put'])
    def apply(self, request, pk, *args, **kwargs):
        user = self.request.user
        try:
            plan = Plan.objects.get(id=pk)
        except Plan.DoesNotExists:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        plan.users.add(user)
        send_mail(
            _('You successfully applied to exercises plan'),
            _('Your exercise changed'),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True,
        )
        return Response({}, status=status.HTTP_200_OK)
