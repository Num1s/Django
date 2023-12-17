from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Show(models.Model):
    GENRE_CHOICES = (
        ('Презентационные видеоролики', 'Презентационные видеоролики'),
        ('Демонстрационные ролики', 'Демонстрационные ролики'),
        ('Испытательные ролики', 'Испытательные ролики'),
        ('Сравнительные ролики', 'Сравнительные ролики'),
        ('Ситуационные ролики', 'Ситуационные ролики'),
    )

    title = models.CharField(max_length=100, verbose_name='Укажите название видео')
    image = models.ImageField(upload_to='youtube_videos/', verbose_name='Укажите превью видео')
    description = models.TextField(verbose_name='Укажите описание видео')
    price = models.PositiveIntegerField(verbose_name='Укажите стоимость видео', validators=[
        MinValueValidator(5),
        MaxValueValidator(20)
    ])
    genre = models.CharField(max_length=100, verbose_name='Укажите жанр видеоролика', choices=GENRE_CHOICES)
    author = models.TextField(verbose_name='Автор видео')
    trailer = models.URLField(verbose_name='Укажите ссылку на видео (Youtube)', default='https://www.youtube.com/')

    def __str__(self):
        return f"{self.title} | {self.description}"
