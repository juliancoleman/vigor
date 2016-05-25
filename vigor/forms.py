from django import forms
from .models import UserPrefs, Meal
from timezone_field import TimeZoneFormField

class MealForm(forms.ModelForm):
    submission_date = forms.DateField(input_formats = ['%d/%m/%Y', '%m/%d/%Y'], required = False)
    meal_name = forms.CharField(required = False)

    def __init__(self, *args, **kwargs):
        date_format = kwargs.pop('date_format')
        super(MealForm, self).__init__(*args, **kwargs)
        self.fields['submission_date'].widget = forms.widget.DateInput(format = date_format)
        self.fields['calories'].widget.attrs = {'placeholder': 320}

    class Meta:
        model = Meal
        exclude = ()

class UserPrefsForm(forms.ModelForm):
    time_zone = TimeZoneFormField()

    class Meta:
        model = UserPrefs
        fields = (
            'first_name',
            'last_name',
            'gender',
            'birth_year',
            'birth_month',
            'birth_day',
            'ethnicity',
            'height_feet',
            'height_inches',
            'weight',
            'time_zone',
            'date_format'
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserPrefs
        fields = ('gender', 'birth_year')
