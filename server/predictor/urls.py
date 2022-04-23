from django.contrib import admin
from django.urls import path

from .views import home,result,yo,sendPredictions

urlpatterns = [
    path('', yo),
    path('result',result)
]