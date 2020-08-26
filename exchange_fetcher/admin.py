from django.contrib import admin
from .models import ExchangeRate


class ExchangeRateAdmin(admin.ModelAdmin):
    readonly_fields = ['exchange_rate', 'bid_price', 'ask_price', 'created_at']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


admin.site.register(ExchangeRate, ExchangeRateAdmin)