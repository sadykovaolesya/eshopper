from django.urls import path 

from .views import  shop, product_details, contact_us

urlpatterns = [
   
    path('shop/', shop, name='shop' ),
    path('product_details/', product_details, name='product_details'),
    path('contact_us/', contact_us, name='contact_us'),
]
