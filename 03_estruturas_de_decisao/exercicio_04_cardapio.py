"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo = int(input("digite o codigo do item"))
quantidade = int(input("digite a quantidade"))

if codigo == 1:
    comida = "Cachorro quente"
    preco = 4.00
elif codigo == 2:
    comida = "X-Salada"
    preco = 4.50
elif codigo == 3:
    comida = "X-Bacon"
    preco = 5.00
elif codigo == 4:
    comida = "Torrada simples"
    preco = 2.00
elif codigo == 5:
    comida = "Refrigerante"
    preco = 1.50
else:
    comida = ("Item invalido")
    preco = 0

total = preco * quantidade

print(f"comida:{comida}")
print(f"Quantidade: {quantidade}")
print(f"Total a pagar: R$ {total:.2f}")
