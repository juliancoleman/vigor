from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('This email is already bound to an existing profile')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
