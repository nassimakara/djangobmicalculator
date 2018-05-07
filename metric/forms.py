from django import forms
from .import models


class Metric(forms.ModelForm):
    class Meta:
        model = models.Metric
        fields = ['height', 'weight']
