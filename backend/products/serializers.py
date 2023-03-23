from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()
