from django.contrib import admin
from django.urls import path, include

from shop.views import greetings, cats, list_item, detail_item

urlpatterns = [
    path('greeting/', greetings),
    path('fact/', cats),
    path('', list_item),
    path('<int:pk>/', detail_item),
]
