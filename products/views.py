from django.shortcuts import render
from django.http import HttpResponse
from . models import product


# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request,'index.html',{'products': products})
    # return HttpResponse("<h1>hallo world</h1>")

def about(request):
    return HttpResponse("<h1>About page</h1>")

def contact(request):
    return HttpResponse('<h1>contact page</h1>')



