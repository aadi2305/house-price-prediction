from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
import pickle

# Create your views here.
def yo(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "index.html")

def result(request):
    return render(request, 'result.html')

class sendPredictions(APIView):
    def post(self,request,format=None):
        model = pickle.load(open('regressorModel.sav', 'rb'))
        prediction = model.predict()
        return Response(request.data, status=status.HTTP_200_OK)

