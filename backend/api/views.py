import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from product.models import Product
from product.serializer import ProductSerializer

from rest_framework.response import Response

# @api_view(["GET"])
# @api_view(["POST"])
@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by("?").first()
    # instance = Product.objects.all().first()
    print("request.GET=> ", request.GET)
    print("request.POST=> ", request.POST)
    print("request.data=> ", request.data)

    ## if GET request
    if request.method=="GET":
        # instance = Product.objects.all()
        query_data = request.GET
        filter = {}
        if "title" in query_data:
            filter["title"] = query_data.get("title")
        if "content" in query_data:
            filter["content"] = query_data.get("content")
        if "price" in query_data:
            filter["price"] = query_data.get("price")

        instance = Product.objects.filter(**filter)
        
        if instance.exists():
            serializer = ProductSerializer(instance, many=True)
            data = {}
            if serializer:
                data = serializer.data

    ## For POST request
    if request.method=="POST":
        serializer = ProductSerializer(data=request.data)
        data = {}

        # if serializer.is_valid():
        #     serializer.save()
        #     data = serializer.data
        #     print("data -> ", data)

        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = ProductSerializer(instance)
        data = serializer.data

    return Response(data, status=200)






