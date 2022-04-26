from django.db.models import *


# Create your models here.
class Feedback(Model):
    user = CharField(max_length=200)
    title = CharField(max_length=200)
    message = TextField()

    def __str__(self):
        return f'{self.user} {self.title}'
