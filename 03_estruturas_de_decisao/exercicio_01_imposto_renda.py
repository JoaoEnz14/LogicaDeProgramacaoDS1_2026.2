"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=int(input("digite seu salario"))
if salario <=2000:
    print("Isento")
elif 2000.01<salario <=3000:
    salario1 = (salario * 0.08)
    print(F"{salario1:.2F}")
elif 3000.01< salario <=4500:
    salario2 = (salario * 0.08) + (salario * 0.18)
    print(F"{salario2:2F}")
elif salario >4500:
    salario3 =(salario * 0.28) + (salario * 0.28)
    print(f"{salario3:2F}")

