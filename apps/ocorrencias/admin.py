from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Ocorrencia


class OcorrenciaAdmin(SimpleHistoryAdmin):
    autocomplete_fields = ['solicitante', 'assunto', 'endereco']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        data = []
        unidades = request.user.unidades.all()
        for unidade in unidades:
            data.append(unidade.id)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(unidade_atual__in=data)


admin.site.register(Ocorrencia, OcorrenciaAdmin)
