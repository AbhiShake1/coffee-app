import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from .models import RewardPoint, OrderHistory
from .shops import SHOPS


# Create your views here.
def shop_list(request: HttpRequest):
    if request.user is None or request.user.is_anonymous:
        return redirect('login')
    return render(request, "shop/shop_list.html",
                  {
                      "shops": SHOPS,
                      "user": request.user,
                  })


@login_required
def shop_menu(request: HttpRequest, slug: str):
    shop = [x for x in SHOPS if x["slug"] == slug][0]
    print(shop)
    return render(request, "shop/shop_menu.html", {"shop": shop})


@login_required
def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    price = data['price']
    action = data['action']
    user = request.user
    if action == 'add':
        OrderHistory.objects.create(user=user, product=productId, price=price)
    return JsonResponse('Item added successfully.', safe=False)


@login_required
def order_history(request):
    user = request.user
    orders = OrderHistory.objects.filter(user=user)
    result = []
    for order in orders:
        result.append({
            'item': order.product,
            'price': order.price,
        })
    return render(request, 'shop/order_history.html', {'orders': result})


@login_required
def rewards(request):
    reward_point = RewardPoint.objects.get(user=request.user).total
    return render(request, 'shop/rewards.html', {
        'reward_point': reward_point,
        'reward_point_width': reward_point % 100,
    })


@login_required
def checkout(request, total):
    try:
        reward = RewardPoint.objects.get(user=request.user)
    except:
        reward = RewardPoint.objects.create(user=request.user, total=0)
    reward.total += (int(total) / 100)
    reward.save()
    return render(request, 'shop/checkout.html', {'total': total, 'reward': reward.total})
