from django.forms import ModelForm
from.models import Composition


class CompForm(ModelForm):
    class Meta:
        model = Composition
        fields = '__all__'