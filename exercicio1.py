import math

def exercicio1():
    raio = float(input("Digite o raio da esfera: "))
    volume = (4 / 3) * math.pi * math.pow(raio, 3)
    print(f"Volume da esfera: {volume:.2f}")

if __name__ == "__main__":
    exercicio1()
