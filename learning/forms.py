from django import forms

from .models import MentoringInfo

class MentoringInfoForm(forms.ModelForm):
    # TODO: make fields Persian
    mentoring_field_title = forms.CharField()
    class Meta:
        model = MentoringInfo
        fields = [
            "mentoring_field_title",
            "road_map"
        ]