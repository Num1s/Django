from django.db import models
from django.contrib.auth.models import User

MALE = 1
FEMALE = 2
UNDEFINED = 3

GENDER_TYPE = (
    ("MALE", "M"),
    ("FEMALE", "Ж"),
    ("UNDEFINED", "-")
)

# Create your models here.
class CustomUser(User):
    name = models.CharField(max_length=100, verbose_name='Укажите имя')
    surname = models.CharField(max_length=100, verbose_name='Укажите фамилию')
    phone_number = models.CharField(max_length=13, default='+996', verbose_name='Укажите номер телефона')
    date_of_birth = models.DateField(verbose_name='Ваша дата рождения')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, verbose_name='Ваш пол')
    hobby = models.CharField(max_length=100, verbose_name='Укажите хобби')
    device = models.CharField(max_length=100, verbose_name='Укажите ваше основное устройство', choices=(
        ('ПК', 'ПК'),
        ('Мобильное устройство', 'Мобильное устройство')
    ))
    social_media = models.CharField(max_length=100, verbose_name='Укажите никнейм в соц сетях')
    marital_status = models.CharField(max_length=100, verbose_name='Укажите семейное положение')
    city = models.CharField(max_length=100, verbose_name='Укажите ваш город проживания')