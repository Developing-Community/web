from django.urls import path

from .views import CreateProductAPIView, ProductListAPIView
urlpatterns = [
    path('product/create/', CreateProductAPIView.as_view(), name="create-product"),
    path('product/list/', ProductListAPIView.as_view(), name="create-product"),
]
