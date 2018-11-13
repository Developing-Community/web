from django import forms

from .models import MentoringInfo


class MentoringInfoForm(forms.ModelForm):
    mentoring_field_title = forms.CharField(label='فیلد مورد نظر', help_text='مثال: برنامه نویسی php')

    class Meta:
        model = MentoringInfo
        fields = [
            "mentoring_field_title",
            "road_map"
        ]

        labels = {
            'road_map': 'نقشه راه'
        }
