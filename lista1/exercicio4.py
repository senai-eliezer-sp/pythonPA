nome = input("Digite seu nome: ")
SalAtual = float(input("Digite seu salario atual: "))
aumento = float(input("Qual foi o aumento do salario: "))

SalNovo = aumento /100 * SalAtual + SalAtual

print(nome,"o seu novo salario é: ", SalNovo)