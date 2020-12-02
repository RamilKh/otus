from django import forms
from app.models import User, Profile
from app.const.models import UserStatuses


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'photo')


class UserCreateForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, min_length=1, required=True)
    last_name = forms.CharField(label='Last name', max_length=100, min_length=1, required=True)
    email = forms.EmailField(label='E-mail', max_length=100, min_length=3, required=True)
    photo = forms.ImageField(label='Фото', required=False)

    field_order = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('department', 'secure_code', 'status')


class ProfileCreateForm(forms.Form):
    department = forms.CharField(max_length=100, min_length=1, required=True)
    secure_code = forms.CharField(max_length=50, min_length=1, required=True)
    status = forms.ChoiceField(label='Status', choices=UserStatuses.choices, required=True)

    field_order = ['department', 'secure_code', 'status']
