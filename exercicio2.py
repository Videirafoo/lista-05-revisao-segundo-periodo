def exercicio2():
    leves = int(input("Quantidade de multas leves: "))
    graves = int(input("Quantidade de multas graves: "))
    gravissimas = int(input("Quantidade de multas gravíssimas: "))

    if gravissimas > 0 or graves > 2:
        classificacao = "Motorista Perigoso"
    elif graves == 2 or leves > 4:
        classificacao = "Motorista Ruim"
    elif graves == 1 or leves > 2:
        classificacao = "Motorista Regular"
    elif leves > 0:
        classificacao = "Motorista Bom"
    else:
        classificacao = "Motorista Excelente"

    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    exercicio2()
