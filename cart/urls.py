from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name="add-cart"),
    path('', views.cart_detail, name="cart-detail")
]