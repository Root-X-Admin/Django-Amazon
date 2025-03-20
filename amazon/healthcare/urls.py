from django.urls import path
from healthcare.views import home, product_list, update_product, delete_product, add_to_cart, view_cart, remove_from_cart, product_buy
from healthcare import views

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('product/update/<int:product_id>/', update_product, name='update_product'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
     path('product/buy/', product_buy, name='product_buy'),
]
