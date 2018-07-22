from django import forms

from .models import Content


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Content

        fields = [
            "title",
            "content"
        ]

        labels = {
            'title': 'عنوان',
            'content': 'متن'
        }
