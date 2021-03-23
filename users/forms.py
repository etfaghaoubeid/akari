from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

user_types = (
('Private Owner', 'Private Owner'),
('Broker', 'Broker'),
)

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    type_of_user = forms.ChoiceField(choices=user_types)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('full_name','phone_number', 'email', 'type_of_user', 'password1', 'password2', )