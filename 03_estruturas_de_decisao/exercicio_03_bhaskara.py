"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo
A = float(input("Digite um número"))
B = float(input("Digite um número"))
C = float(input("Digite um número"))
Delta = (B**2)-(4*A*C)

if A==0 or Delta<0:
    print("Impossivel calcular")
else:
    X1 = (-B + Delta**0.5)/(2*A)
    X2 = (-B - Delta**0.5)/(2*A)
    print(f"sua primeira e{X1:.5f} sua segunda raiz e{X2:.5f}")