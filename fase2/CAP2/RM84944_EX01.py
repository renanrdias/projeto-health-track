import math
peso = float(input("insira seu peso: "))
altura = float(input("insira sua altura: "))

IMC = (peso / (math.pow(altura,2)))

if IMC < 16:
    print("Baixo Peso Grau III")
elif IMC < 17:
    print("Baixo Peso Grau II")
elif IMC < 18.5:
    print("Baixo Peso Grau I")
elif IMC < 25:
    print("Peso ideal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 35:
    print("Obesidade Grau I")
elif IMC < 40:
    print("Obesidade Grau II")
else: 
    print("Obesidade Grau III")




