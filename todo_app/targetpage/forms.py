from django import forms
from targetpage.models import Target


class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = [
            'objective',
            'target_name',
            'expectation_time',
        ]
