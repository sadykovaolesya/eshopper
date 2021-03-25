from django.shortcuts import render

def main(request):
    return render(request, "mainapp/index.html")

def shop(request):
    return render(request, "mainapp/shop.html")

def product_details(request):
    return render(request, "mainapp/product-details.html")

def contact_us(request):
    return render(request, "mainapp/contact-us.html")

