from django.urls import path

from app.views import home, services, service1, preview1, dashboard, my_portfolio, user_list, user_create, user_update, \
    user_read, user_delete

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('service1', service1, name='service1'),
    path('preview1', preview1, name='preview1'),
    path('dashboard', dashboard, name='dashboard'),
    path('portfolio', my_portfolio, name='portfolio'),
    path('list', user_list, name='user_list'),
    path('create/', user_create, name='user_create'),
    path('read/<int:pk>/', user_read, name='user_read'),
    path('update/<int:pk>/', user_update, name='user_update'),
    path('delete/<int:pk>/', user_delete, name='user_delete'),





]