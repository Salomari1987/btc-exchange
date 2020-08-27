from django.urls import path, include
from .views import ExchangeRateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'quotes', ExchangeRateViewSet, basename='rates')


urlpatterns = router.urls
