def exercicio5():
    salario = float(input("Digite o salário bruto: R$ "))

    if salario <= 1500:
        inss = salario * 0.075
    elif salario <= 3000:
        inss = salario * 0.09
    else:
        inss = salario * 0.12

    if salario <= 2000:
        irpf = 0
    elif salario <= 4000:
        irpf = salario * 0.075
    else:
        irpf = salario * 0.15

    salario_liquido = salario - inss - irpf

    print(f"INSS: R$ {inss:.2f}")
    print(f"IRPF: R$ {irpf:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    exercicio5()
