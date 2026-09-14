def exercicio4():
    tipo = input("Digite o tipo de bem (mercadoria ou serviço): ").strip().lower()
    valor = float(input("Digite o valor: R$ "))

    if tipo == "mercadoria":
        imposto = valor * 0.18
        print(f"ICMS devido: R$ {imposto:.2f}")
    elif tipo in ("serviço", "servico"):
        imposto = valor * 0.05
        print(f"ISS devido: R$ {imposto:.2f}")
    else:
        print("Tipo de bem inválido.")

if __name__ == "__main__":
    exercicio4()
