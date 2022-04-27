from django.contrib import admin
from django.urls import path

from .views import home,result,yo,sendPredictions, yo2

urlpatterns = [
    path('', yo),
    path('about',yo2),
    path('result',result)
]