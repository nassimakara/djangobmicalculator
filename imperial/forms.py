from django import forms
from .import models


class Impcalc(forms.ModelForm):
    class Meta:
        model = models.Imperial
        fields = ['heightfeet','heightinches','weightstones','weightpounds']
