from django import forms
from targetpage.models import Target
from django.core.exceptions import ValidationError
import decimal


class TargetForm(forms.ModelForm):
    expectation_time = forms.DecimalField(
        label='完了予想時間',
        min_value=decimal.Decimal(0.1),
        )

    class Meta:
        model = Target
        fields = [
            'objective',
            'target_name',
            'expectation_time',
        ]


class TargetEditForm(forms.ModelForm):
    expectation_time = forms.DecimalField(
        label='完了予想時間',
        min_value=decimal.Decimal(0.1),
    )

    actual_time = forms.DecimalField(
        label='完了実際時間',
        min_value=decimal.Decimal(0.1),
    )

    class Meta:
        model = Target
        fields = '__all__'
