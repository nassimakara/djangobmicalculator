from django.db import models
from django.contrib.auth.models import User


class Metric(models.Model):

    height = models.FloatField(max_length=100)
    weight = models.FloatField(max_length=100)
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


def get_height(self):
        return self.height


def get_weight(self):
        return self.weight


def kgtoimperial(self):
        return self.weight*2.204624


def mtofeet(self):
        return self.height // .3048


def mtoinch(self):
        return self.height / .3048 % 1 * 12


def bmimetrics(self):
        return self.weight/(self.height**2)
