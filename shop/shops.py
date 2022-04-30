from shop.models import Shop


def _get_menus():
    menus = []
    shops = Shop.objects.all()
    for shop in shops:
        menus.append({
            "name": shop.name,
            "image": shop.image,
            "address": shop.address,
            "city": shop.city,
            "slug": shop.slug,
            "menu": {
                "drinks": shop.menu.drinks,
                "snacks": shop.menu.snacks
            }
        })
    return menus


SHOPS = _get_menus()
