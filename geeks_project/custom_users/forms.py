from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

MALE = 1
FEMALE = 2
UNDEFINED = 3

GENDER_TYPE = (
    ("MALE", "M"),
    ("FEMALE", "Ж"),
    ("UNDEFINED", "-")
)

class CustomRegisterForm(UserCreationForm):
    name = forms.CharField(required=True, label='Укажите имя')
    surname = forms.CharField(required=True, label='Укажите фамилию')
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите номер телефона')
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    hobby = forms.CharField(required=True, label='Укажите хобби')
    device = forms.ChoiceField(choices=(
        ('ПК', 'ПК'),
        ('Мобильное устройство', 'Мобильное устройство')
    ), required=False)
    social_media = forms.CharField(required=False, label='Укажите никнейм в соц сетях')
    marital_status = forms.CharField(required=False, label='Укажите семейное положение')
    city = forms.CharField(required=True, label='Укажите город проживания')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'gender',
            'hobby',
            'device',
            'social_media',
            'marital_status',
            'city'
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        
        return user
