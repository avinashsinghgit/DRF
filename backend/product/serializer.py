from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discounted_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ["id","title", "content", "price", "sale_price", "my_discounted_price"]

    def get_my_discounted_price(self, obj):
        # if not hasattr(obj, "id"):
        #     return None
        # if not isinstance(obj, Product):
        #     return None
        return obj.get_discounted_price(20)

