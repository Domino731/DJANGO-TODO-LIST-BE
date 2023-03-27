from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    my_test = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'my_test'
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()

    def get_my_test(self, obj):
        return obj.get_test()
