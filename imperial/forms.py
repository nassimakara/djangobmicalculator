from django import forms
from .import models


class Imperial(forms.ModelForm):
    class Meta:
        model = models.Imperial
        fields = ['heightfeet', 'heightinches', 'weightpounds']
