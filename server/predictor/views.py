from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "../templates/index.html")

def result(request):
    return render(request, 'result.html')