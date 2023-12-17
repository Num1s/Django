from django.urls import path
from . import views

urlpatterns = [
    path('show_list/', views.get_shows, name='show_list'),
    path('show_list/<int:id>/', views.get_show, name='show')
]