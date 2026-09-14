def exercicio3():
    tarefas = []

    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a nova tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso.")

        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa pendente.")
            else:
                for indice, tarefa in enumerate(tarefas, start=1):
                    print(f"{indice} - {tarefa}")

        elif opcao == "3":
            if not tarefas:
                print("Nenhuma tarefa pendente.")
            else:
                for indice, tarefa in enumerate(tarefas, start=1):
                    print(f"{indice} - {tarefa}")

                numero = int(input("Digite o número da tarefa concluída: "))

                if 1 <= numero <= len(tarefas):
                    tarefa = tarefas.pop(numero - 1)
                    print(f"Tarefa concluída: {tarefa}")
                else:
                    print("Tarefa inválida.")

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exercicio3()
