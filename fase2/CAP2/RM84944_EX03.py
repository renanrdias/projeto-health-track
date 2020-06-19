votos_seg = int(input("insira o número de votos na segunda-feira: "))
votos_ter = int(input("insira o número de votos na terça-feira: "))
votos_qua = int(input("insira o número de votos na quarta-feira: "))
votos_qui = int(input("insira o número de votos na quinta-feira: "))
votos_sex = int(input("insira o número de votos na sexta-feira: "))

if votos_seg > votos_ter > votos_qua > votos_qui > votos_sex:
    print("Os votos da segunda-feira ganharam com {} votos".format(votos_seg))
elif votos_ter > votos_qua > votos_qui > votos_sex:
    print("Os votos da terça-feira ganharam com {} votos".format(votos_ter))
elif votos_qua > votos_qui > votos_sex:
    print("Os votos da quarta-feira ganharam com {} votos".format(votos_qua))
elif votos_qui > votos_sex:
    print("Os votos da quinta-feira ganharam com {} votos".format(votos_qui))
else:
    print("os votos da sexta-feira ganharam com {} votos".format(votos_sex))
    


