minutos_atuais = int(input("Insira por favor os minutos que aparecem agora no seu sistema:"))

#calculo do fatorial
fatorial = 1
i = 1
while (i <= minutos_atuais):
    fatorial = fatorial * i 
    i = i + 1
print("A senha para desbloqueio é: LIBERDADE{}".format(fatorial))


