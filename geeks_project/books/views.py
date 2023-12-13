from django.shortcuts import render
from . import models

# Create your views here.
def get_books(request):
    if request.method == 'GET':
        books = models.BookList.objects.all()
        return render(request, template_name='books.html',
                      context={'books': books}
                      )