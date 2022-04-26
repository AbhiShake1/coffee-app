from django.http import HttpRequest
from django.shortcuts import render

from .shops import SHOPS


# Create your views here.
def shop_list(request: HttpRequest):
    print(request.user)
    if request.user is None or request.user.is_anonymous:
        return render(request, "shop/shop_list.html", {"shops": SHOPS, "user": request.user})
    return render(request, "shop/shop_list_logged_in.html", {"shops": SHOPS})


def shop_menu(request: HttpRequest, slug: str):
    shop = [x for x in SHOPS if x["slug"] == slug][0]
    print(shop)
    return render(request, "shop/shop_menu.html", {"shop": shop})
