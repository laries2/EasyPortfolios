from django.urls import path

from app.views import home, services, service1, preview1, dashboard, my_portfolio

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('service1', service1, name='service1'),
    path('preview1', preview1, name='preview1'),
    path('dashboard', dashboard, name='dashboard'),
    path('portfolio', my_portfolio, name='portfolio'),




]