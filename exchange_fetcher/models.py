from django.db import models


class ExchangeRate(models.Model):
    exchange_rate = models.FloatField(blank=False, null=False)
    bid_price = models.FloatField(blank=False, null=False)
    ask_price = models.FloatField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
