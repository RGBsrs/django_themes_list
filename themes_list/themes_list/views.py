from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit

from .models import Theme

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
    # Получаем id выбранных на странице тем из POST запроса
    choosen_themes = list(request.POST.items())[1:]
    choosen_ids = []
    for chosen_theme in choosen_themes:
        choosen_ids.append(int(chosen_theme[1]))

    # Выбираем из базы записи с нужным id
    themes = Theme.objects.filter(pk__in = choosen_ids)

    # генерируем html файл для преобразования в pdf
    template_path = 'pdf_templates/themes_list.html'
    context = {'themes': themes}
    template = get_template(template_path)
    html = template.render(context)
    options = {
        'encoding': "UTF-8",
    }

    # генерация файла
    pdf = pdfkit.from_string(html, False, options)

    # формирования ответа сервера
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    return response



