from django.contrib import admin
from .models import Endereco
from simple_history.admin import SimpleHistoryAdmin


class EnderecoAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Endereco, EnderecoAdmin)
