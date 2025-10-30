# Programa: Estatísticas de um grupo de pessoas

# Listas para armazenar dados
nomes = []
alturas = []
sexos = []
filhos = []

while True:
    print("\n--- Cadastro de Pessoa ---")
    nome = input("Nome: ")
    altura = float(input("Altura (em metros): "))
    sexo = input("Sexo (m/f): ").lower()
    num_filhos = int(input("Número de filhos: "))

    nomes.append(nome)
    alturas.append(altura)
    sexos.append(sexo)
    filhos.append(num_filhos)

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()
    if continuar != 's':
        break

maior_altura = max(alturas)
menor_altura = min(alturas)
nome_maior = nomes[alturas.index(maior_altura)]
nome_menor = nomes[alturas.index(menor_altura)]

alturas_mulheres = [alturas[i] for i in range(len(sexos)) if sexos[i] == 'f']
if len(alturas_mulheres) > 0:
    media_altura_mulheres = sum(alturas_mulheres) / len(alturas_mulheres)
else:
    media_altura_mulheres = 0

total_homens = sum(1 for s in sexos if s == 'm')

media_filhos = sum(filhos) / len(filhos) if len(filhos) > 0 else 0

print(f"a) Maior altura: {maior_altura:.2f} m (Nome: {nome_maior})")
print(f"   Menor altura: {menor_altura:.2f} m (Nome: {nome_menor})")
print(f"b) Média de altura das mulheres: {media_altura_mulheres:.2f} m")
print(f"c) Número total de homens: {total_homens}")
print(f"d) Média de filhos do grupo: {media_filhos:.2f}")
