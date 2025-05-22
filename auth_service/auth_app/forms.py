from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(
        max_length=150,
        required=True,
        help_text='Только буквы, первая заглавная',
        validators=[RegexValidator(r'^[А-ЯЁ][а-яё]+$', 'Только буквы, первая заглавная')],
        label = 'Имя'
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        help_text='Только буквы, первая заглавная',
        validators=[RegexValidator(r'^[А-ЯЁ][а-яё]+$', 'Только буквы, первая заглавная')],
        label='Фамилия'
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
