import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from .shops import SHOPS


# Create your views here.
def shop_list(request: HttpRequest):
    if request.user is None or request.user.is_anonymous:
        return redirect('login')
    return render(request, "shop/shop_list.html", {"shops": SHOPS, "user": request.user})


@login_required
def shop_menu(request: HttpRequest, slug: str):
    shop = [x for x in SHOPS if x["slug"] == slug][0]
    print(shop)
    return render(request, "shop/shop_menu.html", {"shop": shop})


@login_required
def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    return JsonResponse('Item added successfully.', safe=False)


@login_required
def checkout(request, total):
    return render(request, 'shop/checkout.html', {'total': total})
