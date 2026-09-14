def exercicio6():
    alunos = []

    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Exibir alunos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            quantidade = int(input("Quantidade de notas: "))
            notas = []

            for i in range(quantidade):
                nota = float(input(f"Nota {i + 1}: "))
                notas.append(nota)

            alunos.append({"nome": nome, "notas": notas})
            print("Aluno cadastrado com sucesso.")

        elif opcao == "2":
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in alunos:
                    media = sum(aluno["notas"]) / len(aluno["notas"])
                    situacao = "Aprovado" if media >= 7 else "Reprovado"

                    print(f"\nNome: {aluno['nome']}")
                    print(f"Notas: {aluno['notas']}")
                    print(f"Média: {media:.2f}")
                    print(f"Situação: {situacao}")

        elif opcao == "3":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exercicio6()
