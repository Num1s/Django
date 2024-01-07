from django.urls import path
from . import views

urlpatterns = [
    path('parser_houses', views.ParserFormView.as_view(), name='parser_houses')
]