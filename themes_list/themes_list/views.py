from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

from .models import Theme

# Create your views here.
class ThemeHome(ListView):
    model = Theme
    template_name = 'themes_list/index.html'
    context_object_name = 'themes'


def generate(request):
    id = dict(request.POST.items())
    for number in id:
        print(number)
    return redirect('/')

class ShowTheme(DetailView):
    model = Theme
    template_name = 'themes_list/theme.html'
    slug_url_kwarg = 'pk'
    context_object_name = 'theme'
