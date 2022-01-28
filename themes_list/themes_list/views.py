from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from rest_framework import generics

from themes_list.models import Theme
from themes_list.utils import get_themes_ids, html_to_pdf
from themes_list.serializers import ThemeSerializer

class ThemeHome(ListView):
    model = Theme
    template_name = 'themes_list/index.html'
    context_object_name = 'themes'

class ShowTheme(DetailView):
    model = Theme
    template_name = 'themes_list/theme.html'
    slug_url_kwarg = 'pk'
    context_object_name = 'theme'

def generate_pdf(request):
    if request.method == 'POST':
        themes_ids = get_themes_ids(request=request)
        themes = Theme.objects.filter(pk__in = themes_ids)

        template_path = 'pdf_templates/themes_list.html'
        context = {'themes': themes}
        pdf = html_to_pdf(template_path=template_path, context=context)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="themes.pdf"'

        return response
    else:
        return redirect('home')


class ThemeApiView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    lookup_filed = 'pk'
