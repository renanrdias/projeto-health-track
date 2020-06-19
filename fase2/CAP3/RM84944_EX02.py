numero_alunos = 50

#Para os alunos de numero ímpar na chamada
notas_impares = 0
total_impares = 0
for i in range (1,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")
    notas_impares = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(i)))
    total_impares = total_impares + notas_impares
media_impares = total_impares/25

#para os alunos de número par na chamada
notas_pares = 0
total_pares = 0
for p in range(2,51,2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    notas_pares = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}".format(p)))
    total_pares = total_pares + notas_pares
media_pares = total_pares/25

if(media_pares > media_impares):
    print("A média dos alunos de número par na chamada é maior, com valor de {}".format(media_pares))
elif(media_impares > media_pares):
    print("A média dos alunos de número ímpar na chamada é maior, com valor de {}".format(media_impares))
else:
    print("As médias são iguais com o valor de {}".format(media_pares))



