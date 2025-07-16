# Gerenciador de Tarefas
from time import sleep
from os import system

def menu():
    print('===== MENU =====')
    print('1. Adicionar tarefas')
    print('2. Listar tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Remover tarefa')
    print('5. Sair')

def adicionar_tarefa(): 
    add_tarefa=input('Qual tarefa deseja adicionar: ')
    lista_tarefas.append(f'❌ {add_tarefa}')
    return lista_tarefas

def listar_tarefas():
    if len(lista_tarefas)<=0:
        print('Você não tem tarefas')
    else:
        print('===== SUAS TAREFAS =====')
        for indice, tarefa in enumerate(lista_tarefas):
            print(f'[{indice+1}] {tarefa}')

def concluir_tarefa():
    if len(lista_tarefas)<=0:
        print('Você não tem tarefas para concluir')
    else:   
        listar_tarefas()
        resp=input('Qual tarefa você concluiu? ')
        resp=int(resp)
        for indice, tarefa in enumerate(lista_tarefas):
            if indice==(resp-1):
                lista_tarefas[resp-1]=f'✅ {tarefa[2:]}'

def remover_tarefa():
    if len(lista_tarefas)<=0:
        print('Você não tem tarefas para remover')
    else:
        listar_tarefas()
        resp=input('Qual tarefa você quer remover?')
        resp=int(resp)
        lista_tarefas.pop(resp-1)

lista_tarefas=[]

while True:
    menu()
    print()
    escolha=input('Escolha: ')
    system('cls')
    print()
    if escolha=='1':
        adicionar_tarefa()
        sleep(0.5)
    elif escolha=='2':
        listar_tarefas()
        sleep(0.5)
    elif escolha=='3':
        concluir_tarefa()
        sleep(0.5)
    elif escolha=='4':
        remover_tarefa()
        sleep(0.5)
    elif escolha=='5':
        break
    else:
        print('Você digitou a opção errada')
        continue