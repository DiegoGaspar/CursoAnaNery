from django.shortcuts import render,redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista
from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm



def home(request):
    context = {'mensagem':'Ola Mundo'}
    return render(request,'core/index.html', context)

#CRUD_Pessoa
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)  

def pessoa_nova(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def pessoa_update(request, id):
    data={}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa']=pessoa
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoa.html',data)

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method=='POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':pessoa})

#fim CRUD_Pessoa

#CRUD_Veiculo
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos':veiculos, 'form':form}
    return render(request, 'core/lista_veiculos.html', data)        

def veiculo_novo(request):
    form =  VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')

def veiculo_update(request, id):
    data={}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo']=veiculo
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request,'core/update_veiculo.html',data)    

def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method=='POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request,'core/delete_confirm.html',{'obj':veiculo})


#FIM CRUD_Veiculo

#CRUD_MovRotativo
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data ={'form':form, 'mov_rot':mov_rot}
    return render(request, 'core/lista_movrotativos.html',data)

def movrotativos_novo(request):
    form =  MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')

def movrotativos_update(request, id):
    data={}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo']=mov_rotativo
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request,'core/update_movrotativo.html',data)    

def movrotativos_delete(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    if request.method=='POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request,'core/delete_confirm.html',{'obj':mov_rotativo})


#FIM CRUD_MovRotativo

#CRUD_Mensalista
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form':form}
    return render(request, 'core/lista_mensalistas.html', data)

def mensalista_novo(request):
    form =  MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')   

def mensalista_update(request, id):
    data={}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista']=mensalista
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request,'core/update_mensalista.html',data)  

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method=='POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':mensalista})

#FIM CRUD_Mensalista

#CRUD_MovMensalista
def lista_movmensalista(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'form':form,'movmensalistas': movmensalistas}
    return render(request, 'core/lista_movmensalistas.html', data)     

def movmensalista_novo(request):
    form =  MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas') 

def movmensalista_update(request, id):
    data={}
    movmensalistas = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalistas)
    data['movmensalistas']=movmensalistas
    data['form']=form

    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request,'core/update_movmensalista.html',data) 

def movmensalista_delete(request, id):
    movmensalistas = MovMensalista.objects.get(id=id)
    if request.method=='POST':
        movmensalistas.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':movmensalistas})

#FIM CRUD_MovMensalista
