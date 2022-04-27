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
