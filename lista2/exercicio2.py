custo_fab = float(input("Digite o valor de fabrica (R$): "))

imposto = custo_fab * 0.45
lucro_distribuidor = custo_fab * 0.12
preco_consumidor = custo_fab + imposto + lucro_distribuidor

print("O custo de fabrica é: ", custo_fab)
print("Valor do imposto", imposto)
print("Lucro do disbruidor:", lucro_distribuidor)
print("O valor final para o consumidor sera de: ", preco_consumidor)