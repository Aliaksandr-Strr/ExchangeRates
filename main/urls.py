from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExchangeRatesView, price_list_count, MainPage

router = DefaultRouter()
router.register(r'exchange', ExchangeRatesView)
urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('price/', price_list_count, name='download'),
    path('api/', include(router.urls), name='api'),
]