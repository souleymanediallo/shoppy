from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('category/', views.product_category, name="all-category"),
    path('category/<slug:c_slug>/', views.product_category, name="category-by-category")
]