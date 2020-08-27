from rest_framework import viewsets
from .serializers import ExchangeRateSerializer
from .models import ExchangeRate
from rest_framework import status
from rest_framework.response import Response
from .helpers import get_latest_btc_rates
from rest_framework.settings import api_settings


class ExchangeRateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def create(self, request, *args, **kwargs):
        data = get_latest_btc_rates()
        serializer = self.get_serializer(data=data)

        if not serializer.is_valid(raise_exception=False):
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def filter_queryset(self, queryset):
        queryset = self.get_queryset()
        latest_object = queryset.order_by('-created_at').first()

        try:
            return queryset.filter(id=latest_object.id)
        except AttributeError:
            return queryset

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
