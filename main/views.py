from django.shortcuts import render
from main.models import Product

# Create your views here.


def main(request):
    products = Product.objects.all()
    return render(request, "main/main.html", {"products": products})
