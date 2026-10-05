# TODO: Desenvolva o acumulador com parada no 0
soma = 0

numero = int(input("digite um numero"))

while True:
    if numero !=0:
        print("Numero invalido..")
    if numero ==0:
        print("A soma de todos os numeros digitados é:", soma)
        break
    soma += numero
    numero = int(input("Digite outro:"))