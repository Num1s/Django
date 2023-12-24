from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.urls import reverse
from django.http import HttpResponse

# Read.
def get_shows(request):
    if request.method == "GET":
        shows = models.Show.objects.all()
        return render(request, template_name='shows/show_list.html',
                      context={'shows': shows})

def get_show(request, id):
    show = get_object_or_404(models.Show, id=id)
    return render(request, template_name='shows/show.html',
                  context={'show': show})

# Post.
def show_create_view(request):
    if request.method == "POST":
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('/'))

    else:
        form = forms.ShowForm()
        return render(request, template_name='crud/create_show.html',
                      context={'form': form})


# Delete.
def show_delete_view(request):
    if request.method == "GET":
        shows = models.Show.objects.all()
        return render(request, template_name='crud/delete/delete_show.html',
                      context={'shows_delete': shows})

def show_drop_view(request, id):
    show_id = get_object_or_404(models.Show, id=id)
    show_id.delete()
    # return HttpResponse('Success')
    return redirect(reverse('delete_show'))


# Edit.
def show_edit_view(request):
    if request.method == "GET":
        shows = models.Show.objects.all()
        return render(request, template_name='crud/update/update_show.html',
                      context={'shows_update': shows})


def show_update(request, id):
    show_id = get_object_or_404(models.Show, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=show_id, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('update_show'))

    else:
        form = forms.ShowForm(instance=show_id)
        return render(request, template_name='crud/update/edit_show.html',
                      context={
                          "form": form,
                          "show_id": show_id,
                      })