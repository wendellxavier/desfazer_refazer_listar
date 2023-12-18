def show_op(todo_lista):
    print()
    print('Tarefas: ')
    print(todo_lista)
    print()

def op_desfazer(todo_lista, redo_list):
    if not todo_lista:
        print('nada a desfazer')
        return
    
    se_tiver = todo_lista.pop()
    redo_list.append(se_tiver)
    
def op_refazer(todo_lista, redo_list):
    if not redo_list:
        print('nada a refazer')
        return
    
    se_tiver2 = redo_list.pop()
    todo_lista.append(se_tiver2)
    
def add_lista(opcao, todo_lista):
    todo_lista.append(opcao)

if __name__ == '__main__':
    todo_lista = []
    redo_list = []

    while True:
        opcao = input('Digite uma tarefa ou desfazer, refazer, listar: ')

        if opcao == 'listar':
            show_op(todo_lista)
            continue
        elif opcao == 'desfazer':
            op_desfazer(opcao, redo_list)
            continue
        elif opcao == 'refazer':
            op_refazer(opcao, redo_list)
            continue
        add_lista(opcao,todo_lista )