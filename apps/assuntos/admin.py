from django.contrib import admin
from .models import Assunto
from mptt.admin import DraggableMPTTAdmin


class AssuntoAdmin(DraggableMPTTAdmin):
    search_fields = ['nome']
    list_display = ['tree_actions', 'indented_title', 'level', 'folha']
    list_per_page = 100
    expand_tree_by_default = True
    autocomplete_fields = ['unidade']


admin.site.register(Assunto, AssuntoAdmin)
