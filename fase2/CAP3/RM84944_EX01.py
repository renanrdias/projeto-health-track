calorias_total = 0
i = 1
total_alimentos = int(input("Quantos alimentos você ingeriu?"))

while (i <= total_alimentos):
    calorias = float(input("quantas calorias você ingeriu no alimento {}".format(i)))
    calorias_total = calorias_total + calorias
    i = i + 1
 
print("O total de calorias consumidas foi de {}".format(calorias_total))  

    



