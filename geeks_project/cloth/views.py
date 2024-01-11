from django.shortcuts import render
from . import models
from django.views import generic


class AllClothView(generic.ListView):
    template_name = 'cloth/cloth_list.html'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class ManClothView(generic.ListView):
    template_name = 'cloth/cloth_man_list.html'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Мужское')


class WomenClothView(generic.ListView):
    template_name = 'cloth/cloth_women_list.html'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Женское')
    

class KidsClothView(generic.ListView):
    template_name = 'cloth/cloth_kids_list.html'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Детское')
    

class PensionersClothView(generic.ListView):
    template_name = 'cloth/cloth_pensioners_list.html'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Пенсионеры')
