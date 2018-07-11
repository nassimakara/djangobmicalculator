from django.db import models
from django.contrib.auth.models import User


class Imperial(models.Model):

    heightfeet = models.FloatField(max_length=100)
    heightinches = models.FloatField(max_length=100)
    weightpounds = models.FloatField(max_length=100)
    weightstones = models.FloatField(max_length=100)
    heighttometres = models.FloatField(max_length=100)
    bmiimperial = models.FloatField(max_length=100)
    status = models.CharField (max_length=100)
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def get_heightfeet(self):
        return self.heightfeet

    def get_heightinches(self):
        return self.heightinches

    def get_weightpounds(self):
        return self.weightpounds

    def get_weightstones(self):
        return self.weightstones

    def imperialtokg(self):
        return ((self.weightstones * 6.35029318) +(self.weightpounds * 0.45359237))


    def heighttometres(self):
        return (self.heightfeet * 0.3048) + (self.heightinches * 0.0254)


    def bmiimperial(self):
        return ((((self.weightstones * 6.35029318) +(self.weightpounds * 0.45359237))*2.2046226218)* 703) /(((self.heightfeet * 12) + (self.heightinches))**2)


