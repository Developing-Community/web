from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post


class MentoringInfoForm(forms.ModelForm):
    mentoring_fields = forms.CharField()
    class Meta:
        model = Post
        fields = [
            "title",
            "mentoring_fields",
        ]