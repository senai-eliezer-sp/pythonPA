nome = input("Qual o nome do produto: ")
quantidade = int(input("Qual a quantidade que voce deseja adquirir?? "))
preço_uni = float(input("Qual o preço unitario do produto?? "))

total = quantidade * preço_uni


if quantidade <= 20 :
    desconto =  total * 0.2
elif quantidade > 20:
        desconto = total * 0.5
else:
    print("A Qunatidade máxima permitida é 50.")


total_pagar = total - desconto

print("\nProduto: ", nome)
print("Quantidade: ", quantidade)
print("Preço unitário: R$ ", preço_uni)
print("Total bruto: R$ ", total)
print("Desconto: R$ ", desconto)
print("Total a pagar: R$ ", total_pagar)