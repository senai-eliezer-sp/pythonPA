'''Exemplo: criar uma função que calcula o imposto sobre um produto com base
no seu valor.
Nesse caso, a função precisa receber o parâmetro valor, que será o preço do
produto, e, após os cálculos, retornar o valor do imposto com base em faixas
de preço.'''


def calcular_imposto(valor):
 if valor < 1000:
    imposto = valor * 0.1
 elif valor < 2000:
    imposto = valor * 0.13
 else:
    imposto = valor * 0.2
 return imposto

preco_produto = float(input("Digite o preço do produto R$ "))
imposto_produto = calcular_imposto(preco_produto)
print(f"O imposto do produto é de: {imposto_produto}")