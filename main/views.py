import pandas
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import ExchangeRates
from .serializers import ExchangeRatesSerializer


class ExchangeRatesView(viewsets.ModelViewSet):
    queryset = ExchangeRates.objects.all()
    serializer_class = ExchangeRatesSerializer


class MainPage(TemplateView):
    template_name = "main/main.html"


def price_list_count(request):
    queryset = ExchangeRates.objects.all()
    if request.method == 'POST':
        date, usd, eur, rur = [], [], [], []
        for line in queryset:
            date.append(str(line.date))
            usd.append(line.usd)
            eur.append(line.eur)
            rur.append(line.rur)
        d = {'data': date, 'usd': usd, 'eur': eur, 'rur': rur}
        df = pandas.DataFrame(data=d)
        with pandas.ExcelWriter("rates.xlsx", mode="w", options={'remove_timezone': True}) as writer:
            df.to_excel(writer)
        return redirect('/')
    else:
        return render(request, 'main/download.html', )
