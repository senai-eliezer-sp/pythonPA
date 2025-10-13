nome = input("Digite o nome do aluno: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4



if media >= 9 and media <= 10:
    classificacao = "A"
elif media >= 7 and media <=8:
    classificacao = "B"
elif media >= 5 and media <= 6:
    classificacao = "C"
elif media < 5:
    classificacao = "D"
else:
    print("")


print("O nome do aluno é:", nome)
print("A sua media é:", media)
print("Sua classificacao foi:", classificacao)