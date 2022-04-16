from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
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
        print(request.data)
        return HttpResponse(request.data)

def hello(request):
    value1 = request.POST("name")
    return render(request, {"name":value1})
