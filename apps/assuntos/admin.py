from django.contrib import admin
from .models import Assunto
from mptt.admin import DraggableMPTTAdmin


class AssuntoAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'level']
    list_per_page = 100
    expand_tree_by_default = True


admin.site.register(Assunto, AssuntoAdmin)
