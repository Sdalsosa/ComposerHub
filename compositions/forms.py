from django.forms import ModelForm, widgets
from django import forms
from .models import Composition
from taggit.models import Tag

# Make tags a checkbox option for composition creation page


class CompForm(ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Composition
        fields = [
            "title",
            "description",
            "site_link",
            "comp_link",
            "comp_image",
            "tags",
        ]

    def __init__(self, *args, **kwargs):
        super(CompForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter Title"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter Description"}
        )
        self.fields["site_link"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter Website Address"}
        )
        self.fields["comp_link"].widget.attrs.update(
            {"class": "input", "placeholder": "Enter Link Address"}
        )
        self.fields["tags"].widget.attrs.update({"class": "cb-tag"})
