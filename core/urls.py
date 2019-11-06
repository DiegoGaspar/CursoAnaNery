from django.conf.urls import url, include
from .views import (
home, 
lista_pessoas, 
lista_veiculos,
lista_movrotativos,
lista_mensalistas, 
lista_movmensalista, 
pessoa_nova,
veiculo_novo, 
movrotativos_novo,
mensalista_novo, 
movmensalista_novo,
pessoa_update,
veiculo_update,
movrotativos_update,
mensalista_update,
movmensalista_update,
pessoa_delete,
veiculo_delete,
movrotativos_delete,
mensalista_delete,
movmensalista_delete,
confirmacao_cadastro,
)

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^confirmacao/$', confirmacao_cadastro, name='core_confirmacao_cadastro'),


    #URL Pessoa
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoa-novo/$', pessoa_nova, name='core_pessoa_nova'),
    url(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    url(r'^pessoa-delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    
    #URL Veiculo
    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),    
    url(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    url(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    url(r'^veiculo-delete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),

    
    #URL Movimento Rotativo
    url(r'^mov-rot-list/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^mov-rot-novo/$', movrotativos_novo, name='core_movrotativos_novo'),
    url(r'^mov-rot-update/(?P<id>\d+)/$', movrotativos_update, name='core_movrotativos_update'),
    url(r'^mov-rot-delete/(?P<id>\d+)/$', movrotativos_delete, name='core_movrotativos_delete'),


    #URL Mensalista
    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),    
    url(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),
    url(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    url(r'^mensalista-delete/(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),
    

    #URL Movimento Mensalistas
    url(r'^mov-mensalistas/$', lista_movmensalista, name='core_lista_movmensalistas'),
    url(r'^mov-mensal-novo/$', movmensalista_novo, name='core_movmensalista_novo'),
    url(r'^mov-mensal-update/(?P<id>\d+)/$', movmensalista_update, name='core_movmensalista_update'),
    url(r'^mov-mensal-delete/(?P<id>\d+)/$', movmensalista_delete, name='core_movmensalista_delete'),

]