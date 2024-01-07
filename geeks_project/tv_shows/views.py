from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . import models, forms
from django.urls import reverse
from django.http import HttpResponse

class ShowView(generic.ListView):
    template_name = 'shows/show_list.html'
    model = models.Show

    def get_queryset(self):
        return self.model.objects.all()

class GetShow(generic.DeleteView):
    template_name = 'shows/show.html'
    context_object_name = 'show_id'
    model = models.Show

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=show_id)


class ShowCreateView(generic.CreateView):
    template_name = 'crud/create_show.html'
    form_class = forms.ShowForm
    model = models.Show
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowCreateView, self).form_valid(form=form)


# def show_create_view(request):
#     if request.method == "POST":
#         form = forms.ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('/'))

#     else:
#         form = forms.ShowForm()
#         return render(request, template_name='crud/create_show.html',
#                       context={'form': form})


# Delete.
def show_delete_view(request):
    if request.method == "GET":
        shows = models.Show.objects.all()
        return render(request, template_name='crud/delete/delete_show.html',
                      context={'shows_delete': shows})

class ShowDropView(generic.DeleteView):
    template_name = 'crud/delete/confirm_delete.html'
    success_url = '/delete_show/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)

# def show_drop_view(request, id):
#     show_id = get_object_or_404(models.Show, id=id)
#     show_id.delete()
#     # return HttpResponse('Success')
#     return redirect(reverse('delete_show'))


# Edit.
def show_edit_view(request):
    if request.method == "GET":
        shows = models.Show.objects.all()
        return render(request, template_name='crud/update/update_show.html',
                      context={'shows_update': shows})


class ShowUpdateView(generic.UpdateView):
    template_name = 'crud/update/edit_show.html'
    form_class = forms.ShowForm
    success_url = '/update_show/'


    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowUpdateView, self).form_valid(form=form)

# def show_update(request, id):
#     show_id = get_object_or_404(models.Show, id=id)
#     if request.method == 'POST':
#         form = forms.ShowForm(instance=show_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('update_show'))

#     else:
#         form = forms.ShowForm(instance=show_id)
#         return render(request, template_name='crud/update/edit_show.html',
#                       context={
#                           "form": form,
#                           "show_id": show_id,
#                       })
    

class SearchView(generic.ListView):
    template_name = 'shows/show_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Show.objects.filter(title__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context