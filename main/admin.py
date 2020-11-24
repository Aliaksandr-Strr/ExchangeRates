from django.contrib import admin
from .models import ExchangeRates


@admin.register(ExchangeRates)
class ExchangeRatesAdmin(admin.ModelAdmin):
    pass
