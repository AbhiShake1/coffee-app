from django.db.models import *


# Create your models here.
class Order(Model):
    by = ForeignKey('auth.User', on_delete=CASCADE)
