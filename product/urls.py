from .views import GetProductList, CreateOrder
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url


urlpatterns = [
    url(r'^v1/get-product-list/$', csrf_exempt(GetProductList.as_view()), name="product-list"),
    url(r'^v1/create-order/$', csrf_exempt(CreateOrder.as_view()), name="create-product-order"),
]
