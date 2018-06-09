from django import forms

from .models import MyUser


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password',
            'bio',
            'learning_fields_desc',
        ]














