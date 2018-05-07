from django.db import models
from django.contrib.auth.models import User


class Imperial(models.Model):

    heightfeet = models.FloatField(max_length=100)
    heightinches = models.FloatField(max_length=100)
    weightpounds = models.FloatField(max_length=100)
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


def get_heightfeet(self):
        return self.heightfeet

def get_heightinches(self):
        return self.heightinches


def get_weightpounds(self):
        return self.weightpounds


def imperialtokg(self):
        return self.weight*2.204624


def feettometres(self):
        return self.height // .3048


def inchestometres(self):
        return self.height / .3048 % 1 * 12


def bmiimperial(self):
        return self.weight/(self.height**2)
