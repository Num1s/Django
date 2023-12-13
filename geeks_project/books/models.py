from django.db import models

# Create your models here.
class BookList(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    book_name = models.CharField(max_length=40, verbose_name='Book Name')
    book_description = models.TextField(verbose_name='Book Description')
    book_image = models.ImageField(upload_to='', verbose_name='Book Image')
    book_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Book Price')
    book_author = models.CharField(max_length=40, verbose_name='Book Author')
    book_upload_at = models.DateTimeField(auto_now_add=True, verbose_name='Book Upload At')

    def __str__(self):
        return f'{self.book_name} | {self.book_author}'