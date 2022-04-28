from django.db.models import *


# Create your models here.
class Order(Model):
    products = ForeignKey('Cart', on_delete=CASCADE)


class Cart(Model):
    quantity = PositiveIntegerField()
    by = ForeignKey('auth.User', on_delete=CASCADE)
