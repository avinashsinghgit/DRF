from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
import time

# Create your views here.

##   Detail-api-view
class ProductDetailAPIView(generics.RetrieveAPIView):
    lookup_field='pk'
    lookup_url_kwarg = 'product_id'
    def get_object(self):
        obj = super().get_object()
        print("product_id =", self.kwargs['product_id'])
        return super().get_object()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

## Detail-Create-api-view
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(content=content)

# from rest_framework.response import Response

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         obj = super().list(request, *args, **kwargs)
#         data = obj.data
#         modified_data = []
#         for item in data:
#             item.update({"timestamp":time.time()})
#             modified_data.append(item)
#         return Response(data=modified_data )

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        print("🔥 A real request has just hit the API!")
        return super().list(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, *args, **kwargs)
    #     data = response.data

    #     # Add timestamp inside paginated response's "results"
    #     if isinstance(data, dict) and "results" in data:
    #         for item in data["results"]:
    #             item["timestamp"] = time.time()

    #     return response  # ✅ Return full response object — do NOT reconstruct it
    
