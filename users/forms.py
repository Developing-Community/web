from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput,label='کلمه عبور')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("نام کاربری وارد شده وجود ندارد")
                # raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("کلمه عبور نادرست است")
                # raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("نام کاربری غیرفعال است")
                # raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput, label='کلمه عبور')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]

        labels = {
            'username' : 'نام کاربری',
            'email' : 'ایمیل',
            'password' : 'کلمه عبور',
            'first_name' : 'نام',
            'last_name' : 'نام خانوادگی',
        }

        help_texts = {
            'username': None,
        }















