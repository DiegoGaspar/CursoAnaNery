from django.contrib import admin
from .models import Marca,Veiculo,Pessoa, Parametros, MovRotativo, Mensalista, MovMensalista



class MoviRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo','entrada','saida','valor_hora','pago', 'total','horaTotal')


class MovMensalistalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto','total')        



admin.site.register(Marca)
#admin.site.register(Aluno)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MoviRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistalistaAdmin)

