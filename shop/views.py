from django.http import HttpResponse
from django.shortcuts import render
import requests

from shop.models import Item


def greetings(requests):
    return HttpResponse('Добро пожаловать')

def cats(request):
    response = requests.get('https://catfact.ninja/fact').json()
    print(response)
    return HttpResponse(response['fact'])

def list_item(request):
    queryset = Item.objects.all()
    return render(request, 'list_item.html', context={'all_items': queryset})

def detail_item(request, pk, *args, **kwargs):
    item = Item.objects.get(pk=pk)
    return render(request, 'detail_item.html', context={'item':item})






