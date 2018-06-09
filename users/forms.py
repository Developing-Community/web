from django import forms

from .models import MyUser


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput, label='کلمه عبور')

    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password',
            'bio',
            'learning_fields_desc',
        ]

        labels = {
            'username' : 'نام کاربری',
            'email' : 'ایمیل',
            'password' : 'کلمه عبور',
            'bio' : 'معرفی',
            'learning_fields_desc' : 'حوزه های یادگیری',
        }














