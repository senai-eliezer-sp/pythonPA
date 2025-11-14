# Criando uma lista vazia e adicionando valores
meu_vetor = [ ]
meu_vetor.append(10)
meu_vetor.append(25)
print(meu_vetor) # Saída: [10, 25]

# Criando uma lista com valores já definidos
cores = ["vermelho", "azul", "verde"]
print(cores) # Saída: ['vermelho', 'azul', 'verde']
# Adicionando vários valores com um loop for
numeros = [ ]
for i in range(5):
 numeros.append(i)
print(numeros) # Saída: [0, 1, 2, 3, 4]

#                                       #                                                                              #

while contador < 5:
 valor = int(input("Digite um valor: "))
 minha_lista.append(valor)
 contador += 1
print(minha_lista)
try:
 x=int(input("Qual dos 5 valores você quer visualizar da lista: "))
 if 1 <= x <= len(minha_lista):
 valor = minha_lista[x-1]
 print(f"O valor guardado no índice {x} é: {valor}")
 else:
 print("Erro: Índice fora do intervalo válido.")
except ValueError:
 print("Erro: Entrada inválida. Digite um número inteiro.")

 #                                       #                                                                           #

 # Definindo as cores como constantes para facilitar o uso
VERMELHO = '\033[1;31m'
VERDE = '\033[3;32m'
AZUL = '\033[0;34m'
BRANCO_MAGENTA = '\033[1;37;45m'
NORMAL = '\033[0m' # Código para resetar a cor para o padrão
print(f'{VERMELHO}Este texto está em vermelho negrito.{NORMAL}')
print(f'{VERDE}Este texto está em verde e itálico.{NORMAL}')
print(f'{AZUL}Este texto está em azul.{NORMAL}')
print(f'{BRANCO_MAGENTA}Este texto está em branco negrito com fundo
magenta.{NORMAL}')