from django.urls import path, include
from .views import ProductDetailAPIView

urlpatterns = [
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail_api_view")
]


