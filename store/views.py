from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Create your views here.
def index(request):
    return HttpResponse("Mm Online Fashions")

"""This view will handle requests for a list of all categories
It uses generic ListAPIView to fetch multiple objects"""
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(generics.RetrieveAPIView):
    """Handle requests for a single category by ID
    Uses a generic RetrieveAPIView to fetch one specific
    object"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class BrandList(generics.ListAPIView):
    """fetches a list of all brands"""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class BrandDetail(generics.RetrieveAPIView):
    """Fetches a brand by ID"""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
class ProductList(generics.ListAPIView):
    """ Handles requests for a List of all Products """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetail(generics.RetrieveAPIView):
    """fetches a single product based on ID"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer