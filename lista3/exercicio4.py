'''Calculador: Solicitar ao usuário, entrar com 2 valores e o operador (+, -, * ou /) e executar
o cálculo e mostrar o resuiltado a partir do operador escolhido (resolver usando o comando
escolha-caso)'''

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == '+':
    resultado = valor1 + valor2
elif operador == '-':
    resultado = valor1 - valor2
elif operador == '*':
    resultado = valor1 * valor2
elif operador == '/':
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operador inválido"

print("Resultado: ", resultado)



