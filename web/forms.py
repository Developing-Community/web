from django import forms

from users.models import Profile


class SharifSummerMarketProfileTempForm(forms.ModelForm):
    complete_name = forms.CharField(max_length=255,
                                    label='',
                                    widget=forms.TextInput
                                    (attrs={'placeholder': 'نام و نام خانوادگی'
                                            }))
    phone = forms.CharField(max_length=20,
                            label='',
                            widget=forms.TextInput
                            (attrs={'placeholder': 'شماره تماس'}))

    def __init__(self, *args, **kwargs):
        super(SharifSummerMarketProfileTempForm, self).__init__(*args, **kwargs)
        self.fields['complete_name'].required = True
        self.fields['phone'].required = True

    class Meta:
        model = Profile

        fields = [
            'complete_name',
            'phone',
        ]

        labels = {
            'complete_name': 'نام و نام خانوادگی',
            'phone': 'شماره تماس'
        }
