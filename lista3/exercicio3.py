nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc =  peso / (altura * altura)

if imc <= 18:
    print("Você está a baixo do peso.")
elif imc >18 and imc <= 24:
    print("Seu peso está normal.")
elif imc > 24:
    print("Você está obeso, Procure a academia mais proxima!!")

print(nome," o resultado do seu IMC é: ", imc)