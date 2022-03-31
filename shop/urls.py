from django.urls import path
from .views import shop_list, shop_menu

urlpatterns = [
    path("", shop_list, name="home"),
    path("menu/<str:slug>/", shop_menu, name="menu"),
]
