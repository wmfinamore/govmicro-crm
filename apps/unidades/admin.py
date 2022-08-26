from django.contrib import admin
from .models import Unidade
from mptt.admin import DraggableMPTTAdmin


class UnidadeAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'level']
    filter_horizontal = ('funcionarios', )
    fieldsets = (
        (None,
             {'fields':
                 ('nome', 'sigla', 'ativo', 'parent', 'funcionarios'),
             },
         ),
    )
    search_fields = ['nome', 'sigla']


admin.site.register(Unidade, UnidadeAdmin)
