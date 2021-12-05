from django.template.loader import get_template
import pdfkit

def get_themes_ids(request=None):
    if request:
        themes= list(request.POST.items())[1:]
        ids = []
        for theme_id in themes:
            ids.append(int(theme_id[1]))
        return ids
    else:
        return []

def html_to_pdf(template_path:str, context:dict):
    template = get_template(template_path)
    html = template.render(context)
    options = {
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    return pdf
