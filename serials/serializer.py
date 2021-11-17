from rest_framework import serializers
from .models import Product,Category,ProductImage


class ImageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields=['image','alt_text']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['id','title','description','category','amount','rating','country','year','created_at','slug']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =['name','slug']    