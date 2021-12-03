from django.contrib import admin
from .models import Theme

# Register your models here.


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Theme, ThemesAdmin)