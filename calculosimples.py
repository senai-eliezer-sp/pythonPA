'''
        exemlo calculo simples

a = float(input("Digite o primeiro valor: "))
b =  float (input("Digite o segundo valor: "))
soma = a + b
print("A soma dos valores é: ", soma)'''





'''              Estrutura Condicionais                '''

'''idade = int(input("Digite sua idade: "))
if idade >=18:
    print("Maior de idade.")
else:
    print("Menor de idade.")  '''



'''               Exemplo com multiplas condições      '''

'''nota = float(input("Digite sua nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")'''

'''            Uso de operadores logicos e condicionais '''

idade = int(input("Digite a sua idade: "))
habilitado = input("Possui carteira de motorista? (s/n): ")
if idade >= 18 and habilitado == "s":
    print("Voce pode dirigir.")
else:
    print("Não pode dirigir.")