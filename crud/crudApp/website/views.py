from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'website/index.html')
def login(request):
    return render(request, 'website/login.html')