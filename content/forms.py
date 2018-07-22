from django import forms

from .models import Content


class ArticleForm(forms.ModelForm):
    subject_title = forms.CharField(label='موضوع')
    # publish = forms.DateField(widget=forms.SelectDateWidget, label='تاریخ انتشار')

    class Meta:
        model = Content

        fields = [
            "title",
            "subject_title",
            # "image",
            "content",
            # "publish"
        ]

        labels = {
            'title': 'عنوان',
            # 'image' : 'تصویر',
            'content': 'متن',
        }