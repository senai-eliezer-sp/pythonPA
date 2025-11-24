def desconto(qt, tt):
    if qt <= 20:
        return tt * 0.02
    else:
        return tt * 0.06

nome = input("Qual o nome do produto: ")
preço_uni = float(input("Qual o preço unitario do produto?? "))


while True:
    quantidade = int(input("Digite a quantidade de (max. 50): "))
    if quantidade <= 50:
        break

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