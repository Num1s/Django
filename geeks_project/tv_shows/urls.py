from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('', views.ShowView.as_view(), name='show_list'),
    path('show_list/<int:id>/', views.GetShow.as_view(), name='show'),
    path('create_show/', views.ShowCreateView.as_view(), name='create_show'),
    path('delete_show/', views.show_delete_view, name='delete_show'),
    path('drop_show/<int:id>/delete', views.ShowDropView.as_view(), name='drop_show'),
    path('update_show/', views.show_edit_view, name='edit_show'),
    path('edit_show/<int:id>/edit', views.ShowUpdateView.as_view(), name='update_show'),
    path('search/', views.SearchView.as_view(), name='search')
]