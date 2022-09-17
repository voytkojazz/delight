from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ingridients/', views.IngridientView.as_view(), name='ingridients-list'),
    path('menu/', views.MenuItemListView.as_view(), name='menu-items-list'),
    path('purchases/',  views.PurchaseListView.as_view(), name='purchase-list'),
    path('profit-revenue/', views.ProfitRevenueView.as_view(), name='profit-revenue'),
]
