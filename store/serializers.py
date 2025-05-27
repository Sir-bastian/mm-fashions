""" Serializer module.
This module will convert Django models into
a format that is standardized like JSON"""

from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
    
class ProductSerializer(serializers.ModelSerializer):

    # This field will serialize the 'name' of the related Category object
    # read_only=True means this field won't be used when creating/updating products via API
    # source='category.name' tells it to look at the 'name' attribute of the 'category' object

    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock', 'sku', 'image_url',
            'created_at', 'updated_at', 'category_name', 'brand_name'
        ]