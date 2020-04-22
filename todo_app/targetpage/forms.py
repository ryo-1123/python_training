from django import forms
from targetpage.models import Target
from django.core.exceptions import ValidationError


class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = [
            'objective',
            'target_name',
            'expectation_time',
        ]

    def clean_expectation_time(self):
        expectation_time = self.cleaned_data.get('expectation_time')
        if expectation_time <= 0:
            raise forms.ValidationError('0以上の数を入力してください。')
        return expectation_time
