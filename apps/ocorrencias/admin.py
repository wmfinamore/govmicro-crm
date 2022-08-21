from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Ocorrencia


class OcorrenciaAdmin(SimpleHistoryAdmin):
    autocomplete_fields = ['solicitante', 'assunto', 'endereco']


admin.site.register(Ocorrencia, OcorrenciaAdmin)
