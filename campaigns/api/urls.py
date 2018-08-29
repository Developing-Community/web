from django.urls import path

from campaigns.api.views import CreateProductAPIView
urlpatterns = [
    path('product/create/', CreateProductAPIView.as_view(), name="create-product"),
]
