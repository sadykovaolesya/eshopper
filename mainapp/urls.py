from django.urls import path 

from .views import index, shop, product_details, contact_us

urlpatterns = [
    path('', index),
    path('shop/', shop),
    path('product_details/', product_details),
    path('contact_us/', contact_us),
]
