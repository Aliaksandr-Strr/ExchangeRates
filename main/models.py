from django.db import models


class ExchangeRates(models.Model):
    date_today = models.DateTimeField(auto_now_add=True)
    usd = models.DecimalField(max_digits=10, decimal_places=3)
    eur = models.DecimalField(max_digits=10, decimal_places=3)
    rur = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'Курсы валют'
        ordering = ['date_today']
