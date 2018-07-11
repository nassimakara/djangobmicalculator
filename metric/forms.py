from django import forms
from .import models


class Mcalc(forms.ModelForm):
    class Meta:
        model = models.Metric
        fields = ['height', 'weight']



