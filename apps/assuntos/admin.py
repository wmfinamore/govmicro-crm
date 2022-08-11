from django.contrib import admin
from .models import Assunto
from mptt.admin import MPTTModelAdmin


class AssuntoAdmin(MPTTModelAdmin):
    list_display = ['id', 'nome', 'level']


admin.site.register(Assunto, AssuntoAdmin)
