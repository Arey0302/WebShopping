from django.shortcuts import render
from django.http import HttpResponseGone

# Create your views here.
def home(request):
    return render(request,'app/home.html')