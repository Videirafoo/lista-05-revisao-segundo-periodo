from exercicio1 import exercicio1
from exercicio2 import exercicio2
from exercicio3 import exercicio3
from exercicio4 import exercicio4
from exercicio5 import exercicio5
from exercicio6 import exercicio6


def main():
    exercicios = {
        "1": exercicio1,
        "2": exercicio2,
        "3": exercicio3,
        "4": exercicio4,
        "5": exercicio5,
        "6": exercicio6,
    }

    while True:
        print("\nRevisão de Algoritmos")
        print("1 - Exercício 1")
        print("2 - Exercício 2")
        print("3 - Exercício 3")
        print("4 - Exercício 4")
        print("5 - Exercício 5")
        print("6 - Exercício 6")
        print("0 - Sair")

        opcao = input("Escolha um exercício: ")

        if opcao == "0":
            break

        exercicio = exercicios.get(opcao)
        if exercicio is None:
            print("Opção inválida.")
            continue

        exercicio()


if __name__ == "__main__":
    main()