faturamento = float(input("Insira seu faturamento: "))
plano = input("Insira o seu plano: ")

if plano.lower() == "basic":
    bonus = 0.3 * faturamento
elif plano.lower() == "silver":
    bonus = 0.2 * faturamento
elif plano.lower() == "gold":
    bonus = 0.1 * faturamento
elif plano.lower() == "platinum":
    bonus = 0.05 * faturamento
else:
    print("Plano incorreto. Tente novamente!")
    
print("o valor do bonus é R$ {}".format(bonus))



