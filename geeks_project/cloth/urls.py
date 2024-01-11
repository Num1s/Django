from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.AllClothView.as_view()),
    path('man_cloth/', views.ManClothView.as_view()),
    path('women_cloth/', views.WomenClothView.as_view()),
    path('kids_cloth/', views.KidsClothView.as_view()),
    path('pensioners_cloth/', views.PensionersClothView.as_view()),
]