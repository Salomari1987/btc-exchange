from rest_framework import viewsets
from .serializers import ExchangeRateSerializer
from .models import ExchangeRate
from rest_framework import status
from rest_framework.response import Response
from .helpers import get_latest_btc_rates


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

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



