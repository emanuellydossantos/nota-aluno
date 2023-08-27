nome = input("Nome do(a) aluno(a): ")
n1 = float(input("Nota: "))
n2 = float(input("Nota: "))
media = (n1 + n2) / 2
print ("A média é:    ",media)
print()
if media >= 6:
    print ("Aprovado(a)")
    print ("Parabéns!")
elif media < 6 or media > 3:
    print ("Recuperação")
    print ("Boa sorte na prova!")
else:
    print ("Repetiu de ano")
    print ("  ):")
print ()
print()
perg = input("Continuar? Coloque 'Sim' ou 'Não': ")
print()
print()
while True:
    if perg == "Sim" or perg == "sim":
        nome = input("Nome do(a) aluno(a):  ")
        n1 = float(input("Nota: "))
        n2 = float(input("Nota: "))
        media = (n1 + n2) / 2
        print ("A média é: ",media)
        print()
        if media >= 6:
            print ("Aprovado(a)")
            print ("Parabéns!")
        elif media < 6 and media > 3:
            print ("Recuperação")
            print ("Boa sorte na prova!") 
        else:
            print ("Repetiu de ano")
            print ("  ):")
        print()
        print()
        perg = input("Continuar? Coloque 'Sim' ou 'Não': ")
        print ()
        print()
        continue
    elif (perg == "Não" or perg == "não"):
        print("O programa foi encerrado")
        break
    else:
        print ("Você não escreveu 'Sim' ou 'Não'")
        print ("O programa foi encerrado")
        break
