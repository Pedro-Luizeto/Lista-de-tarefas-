from time import sleep


def espaco():
    print('')
def linha():
    print('----------------------------------------')

tarefas = []

while True:
    print('=== L I S T A   D E   T A R E F A S ===')
    sleep(1)
    espaco()
    linha()
    print('[1] - Adicionar tarefa')
    print('[2] - Remover tarefa')
    print('[3] - Listar tarefas')
    print('[4] - Tarefas pendentes')
    print('[5] - Sair')
    espaco()
    escolha = input('Escolha uma opção: ')
    espaco()
    linha()

    match escolha:
        case '1':
            print('=== ADICIONAR TAREFA ===')
            espaco()
            tarefa = input('Digite a tarefa que deseja adicionar: ')
            tarefas.append(tarefa)
            print(f'Tarefa "{tarefa}" adicionada com sucesso!')
            espaco()
            linha()

        case '2':
            print('=== REMOVER TAREFA ===')
            espaco()
            if not tarefas:
                print('Não há tarefas para remover.')
            else:
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f'{i}. {tarefa}')
                espaco()
                indice = int(input('Digite o número da tarefa que deseja remover: '))
                if 1 <= indice <= len(tarefas):
                    tarefa_removida = tarefas.pop(indice - 1)
                    print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
                else:
                    print('Índice inválido. Nenhuma tarefa foi removida.')
                    espaco()


        case '3':
            print('=== LISTA DE TAREFAS ===')
            espaco()
            if not tarefas:
                print('Não há tarefas na lista.')
            else:
                print('Tarefas na lista:')
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f'{i}. {tarefa}')


        case '4':
            print('=== TAREFAS PENDENTES ===')
            espaco()
            if not tarefas:
                print('Não há tarefas pendentes.')
            else:
                print('Tarefas pendentes:')
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f'{i}. {tarefa}')


        case '5':
            print('Saindo do programa...')
            break



        case _:
            print('Opção inválida. Por favor, escolha uma opção válida.')

