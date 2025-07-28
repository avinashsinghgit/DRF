from django.urls import path, include
from .views import ProductDetailAPIView, ProductCreateAPIView, ProductListAPIView

urlpatterns = [
    path("create/", ProductCreateAPIView.as_view(), name='product_create_api_view'),
    path("", ProductListAPIView.as_view(), name='product_list_api_view'),
    path("<int:product_id>/", ProductDetailAPIView.as_view(), name="product_detail_api_view"),
]



