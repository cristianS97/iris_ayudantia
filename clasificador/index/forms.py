from django import forms
from django.forms import widgets

class IrisForm(forms.Form):
    sepal_length = forms.FloatField(
        label='Largo del sepalo',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'step': 0.1
            }
        )
    )
    sepal_width = forms.FloatField(
        label='Ancho del sepalo',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'step': 0.1
            }
        )
    )
    petal_length = forms.FloatField(
        label='Largo del pétalo',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'step': 0.1
            }
        )
    )
    petal_width = forms.FloatField(
        label='Ancho del pétalo',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'step': 0.1
            }
        )
    )

