from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_stores = Store.objects.all()
    all_items = Item.objects.all()
    all_lists = ShopList.objects.all()
    return render(request, 'life/index.html', {"stores":all_stores, "items":all_items, "lists":all_lists})