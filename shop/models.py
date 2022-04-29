from django.db.models import *


# Create your models here.
class Shop(Model):
    name = CharField(max_length=200)
    image = CharField(max_length=1000)
    address = CharField(max_length=200)
    city = CharField(max_length=200)
    slug = CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Menu(Model):
    drinks = JSONField()
    snacks = JSONField()
    shop = OneToOneField(Shop, on_delete=CASCADE)

    def __str__(self):
        return str(self.shop.name)


class RewardPoint(Model):
    user = OneToOneField('auth.User', on_delete=CASCADE)
    total = PositiveIntegerField()


class OrderHistory(Model):
    user = CharField(max_length=200)
    product = CharField(max_length=200)
    price = PositiveIntegerField()

    def __str__(self):
        return f'user: {self.user}, product: {self.product}, price: {self.price}'
