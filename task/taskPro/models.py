from django.db import models


class Task(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return "Name:{},Description:{},price:{}".format(self.name, self.description, self.price)
