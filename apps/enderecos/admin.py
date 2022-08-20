from django.contrib import admin
from .models import Endereco
from simple_history.admin import SimpleHistoryAdmin


class EnderecoAdmin(SimpleHistoryAdmin):
    search_fields = ['endereco', 'bairro', 'cidade', 'estado', 'cep', ]


admin.site.register(Endereco, EnderecoAdmin)
