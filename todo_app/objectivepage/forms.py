from django import forms
from objectivepage.models import Objective


class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = [
            'object_name',
            'object_category',
            'user',
        ]
        widgets = {'user': forms.HiddenInput()}
