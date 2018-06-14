from django import forms

from .models import MyUser


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput, label='کلمه عبور')

    class Meta:
        model = MyUser
        fields = [
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
        ]

        labels = {
            'username' : 'نام کاربری',
            'first_name' : 'نام',
            'last_name' : 'نام خانوادگی',
            'email' : 'ایمیل',
            'password' : 'کلمه عبور',
        }














