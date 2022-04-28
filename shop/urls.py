from django.urls import path

from .views import shop_list, shop_menu, update_item, checkout

urlpatterns = [
    path("", shop_list, name="home"),
    path("menu/<str:slug>/", shop_menu, name="menu"),
    path("update_item/", update_item, name="update_item"),
    path("checkout/total=<int:total>/", checkout, name="checkout"),
]
