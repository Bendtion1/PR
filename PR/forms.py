# Django
from django import forms

# Local Django
from . models import *


class CreateImpressionForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Название", "class": "form-control"}
        ),
        label="Название",
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Описание", "class": "form-control"}
        ),
        label="Описание",
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите адрес",
                "class": "form-control",
            }
        ),
        label="Поиск",
        max_length=200,
        required=False,
    )

    location = PlainLocationField(
        based_fields=["address"],
        zoom=8,
    )

    class Meta:
        model = Impression
        fields = ["title", "content", "address", "location"]
