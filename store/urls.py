from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # Path for retrieving, updating, or deleting a specific category
    # Example: /api/categories/1/ (where 1 is the category's ID)
    path("categories/", views.CategoryList.as_view(), name="category-list" ),
    path("categories/<int:pk>", views.CategoryDetail.as_view(), name="category-detail" ),
    
    # Path for retrieving, updating, or deleting a specific Brand
    # Example: /api/categories/1/ (where 1 is the Brand's ID)
    path("brands/", views.BrandList.as_view(), name="brand-list"),
    path("brands/<int:pk>", views.BrandDetail.as_view(), name="brand-detail"),
    
    # Path for retrieving, updating, or deleting a specific product
    # Example: /api/categories/1/ (where 1 is the product's ID)
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),
]