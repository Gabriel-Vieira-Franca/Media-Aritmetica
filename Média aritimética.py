NOME = input("Digite o nome do Aluno: ")
BIM1 = float(input("Digite a Nota do Primeiro Bimestre: "))
BIM2 = float(input("Digite a Nota do Segundo Bimestre: "))
BIM3 = float(input("Digite a Nota do Terceiro Bimestre: "))
BIM4 = float(input("Digite a Nota do Quarto Bimestre: "))

MEDIA = float((BIM1+BIM2+BIM3+BIM4)/4)

print ("A média anual do aluno", NOME, "é:", MEDIA)
    
if MEDIA >= 9:
    print ("Você foi aprovado com louvor")
    
elif MEDIA >= 7:
    print ("Você foi aprovado")

elif MEDIA <5:
    print("Você foi reprovado")
    
elif MEDIA <7:
    print("Você está de recuperação")