from django.urls import path
from .views import *

urlpatterns=[
    path("productdet/<int:id>",ProductDetailsView.as_view(),name="prodet"),
    path("addtocart/<int:id>",AddtoCartView.as_view(),name="acart"),
    path("cartview",CartListView.as_view(),name="cartview"),
    path("remcart/<int:id>",DeleteCartView.as_view(),name="rcart"),
    path("checkout/<int:id>",CheckoutView.as_view(),name="cout"),
    path("orderlist",OrderListView.as_view(),name="olist"),
    path("Cancelorder/<int:id>",Cancelorder,name="corder"),
    path("addreview/<int:id>",addreview,name="addrev")
]