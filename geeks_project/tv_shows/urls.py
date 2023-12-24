from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_shows, name='show_list'),
    path('show_list/<int:id>/', views.get_show, name='show'),
    path('create_show/', views.show_create_view, name='create_show'),
    path('delete_show/', views.show_delete_view, name='delete_show'),
    path('drop_show/<int:id>/delete', views.show_drop_view, name='drop_show'),
    path('update_show/', views.show_edit_view, name='edit_show'),
    path('edit_show/<int:id>/edit', views.show_update, name='update_show')
]