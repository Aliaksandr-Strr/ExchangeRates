import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import ExchangeRates


class Command(BaseCommand):
    help = 'Сохраняет в БД актуальный курс валют'

    def handle(self, *args, **options):
        response = requests.get(settings.CBR_API_URL)
        curs = response.json()
        rur = curs['rates'][3]['buyRate'] / 100
        eur = curs['rates'][4]['buyRate']
        usd = curs['rates'][5]['buyRate']
        ExchangeRates.objects.create(usd=usd, eur=eur, rur=rur)
