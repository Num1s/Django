from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def get_shows(request):
    if request.method == "GET":
        shows = models.Show.objects.all()
        return render(request, template_name='shows/show_list.html',
                      context={'shows': shows})

def get_show(request, id):
    show = get_object_or_404(models.Show, id=id)
    return render(request, template_name='shows/show.html',
                  context={'show': show})