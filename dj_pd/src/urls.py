from django.urls import path
from . import views

app_name = 'src'

urlpatterns = [
    path('', views.chart_select_view, name='main-products-view'),
    path('add/', views.add_purchase_view, name='add-purchase-view'),
]