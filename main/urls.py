from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ExchangeRatesView, price_list_count

router = DefaultRouter()
router.register(r'exchange', ExchangeRatesView)
urlpatterns = [
    path('price/', price_list_count, name='download'),
]
urlpatterns += router.urls
