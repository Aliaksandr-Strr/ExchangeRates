import pandas
import requests
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import ExchangeRates
from .serializers import ExchangeRatesSerializer
from django.conf import settings


def func():
    response = requests.get(settings.CBR_API_URL)
    day_result = response.json()
    rur = day_result['rates'][3]['buyRate'] / 100
    eur = day_result['rates'][4]['buyRate']
    usd = day_result['rates'][5]['buyRate']
    ExchangeRates.objects.create(usd=usd, eur=eur, rur=rur)


class ExchangeRatesView(viewsets.ModelViewSet):
    func()
    queryset = ExchangeRates.objects.all()
    serializer_class = ExchangeRatesSerializer


def price_list_count(request):
    queryset = ExchangeRates.objects.all()
    if request.method == 'POST':
        date, usd, eur, rur = [], [], [], []
        for line in queryset:
            date.append(str(line.date_today))
            usd.append(line.usd)
            eur.append(line.eur)
            rur.append(line.rur)
        print(date, usd)
        d = {'data': date, 'usd': usd, 'eur': eur, 'rur': rur}
        df = pandas.DataFrame(data=d)
        with pandas.ExcelWriter("rates.xlsx", mode="w", options={'remove_timezone': True}) as writer:
            df.to_excel(writer)
        return redirect('/')
    else:
        return render(request, 'main/download.html', )
