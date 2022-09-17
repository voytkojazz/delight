from pipes import Template
from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, View, TemplateView
from .models import Ingridient, MenuItem, Purchase
# Create your views here.





class IngridientView(View):
    def get(self, request):
        all_ingridients = Ingridient.objects.all()
        context = {
            'all_ingridients': all_ingridients,
        }
        return render(request, 'inventory/ingridients-list.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            ingridients_ids = request.POST.getlist('id[]')
            for id in ingridients_ids:
                ingridient = Ingridient.objects.get(pk=id)
                ingridient.delete()
            return redirect('ingridients-list')



class MenuItemListView(ListView):
    model = MenuItem
    context_object_name = 'menu_items_list'
    template_name = 'inventory/menu-items-list.html'


class PurchaseListView(TemplateView):
    purchases_list = Purchase.objects.all()
    template_name = 'inventory/purchase-list.html'

    purchases = {}

    for purchase in purchases_list:
        purchase_rr = purchase.menu_item.reciperequirement_set.all()
        purchase_revenue = 0
        for rr in purchase_rr:
            price = rr.ingridient.unit_price
            quantity = rr.quantity
            purchase_revenue += price * quantity

        purchases[purchase] = {
            'menu_item': None,
            'timestamp': None,
            'profit': None,
        }



        purchases[purchase]['menu_item'] = purchase.menu_item.title
        purchases[purchase]['timestamp'] = purchase.timestamp
        purchases[purchase]['profit'] = purchase.menu_item.price - purchase_revenue

    for purchase in purchases.values():
        print(purchase['menu_item'])
        print(purchase['profit'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases_dict'] = self.purchases
        return context


class ProfitRevenueView(TemplateView):
    template_name = 'inventory/profit-revenue.html'

    revenue = 0
    profit = 0

    purchases = Purchase.objects.all()

    for purchase in purchases:
        revenue += purchase.menu_item.price
        purchase_rr = purchase.menu_item.reciperequirement_set.all()
        purchase_revenue = 0

        for rr in purchase_rr:
            quantity = rr.quantity
            price = rr.ingridient.unit_price
            purchase_revenue = quantity * price

        purchase_profit = purchase.menu_item.price - purchase_revenue

        profit += purchase_profit

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['revenue'] = self.revenue
        context['profit'] = self.profit
        return context


class Home(TemplateView):
    template_name = 'inventory/home.html'
    