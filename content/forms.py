from django import forms
from django.utils import timezone

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

class ReportForm(forms.ModelForm):
    subject_title = forms.CharField(label='موضوع')
    publish = forms.DateField(widget=forms.SelectDateWidget, label='تاریخ', initial=timezone.now())

    class Meta:
        model = Content

        fields = [
            "title",
            "subject_title",
            # "image",
            "content",
            "publish"
        ]

        labels = {
            'title': 'عنوان',
            # 'image' : 'تصویر',
            'content': 'متن',
            'note': 'یادداشت'
        }

        help_texts = {
            'note' : 'اگر تمایل داشتید نکاتی درباره چیزهایی که یاد گرفتید بنویسید'
        }
