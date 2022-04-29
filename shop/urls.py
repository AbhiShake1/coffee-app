from django.urls import path

from .views import shop_list, shop_menu, update_cart, checkout, order_history

urlpatterns = [
    path("", shop_list, name="home"),
    path("menu/<str:slug>/", shop_menu, name="menu"),
    path("update_cart/", update_cart, name="update_cart"),
    path("checkout/total=<int:total>/", checkout, name="checkout"),
    path("order_history/", order_history, name="order_history"),
]
