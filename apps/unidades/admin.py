from django.contrib import admin
from .models import Unidade
from mptt.admin import DraggableMPTTAdmin


class UnidadeAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'level']


admin.site.register(Unidade, UnidadeAdmin)
