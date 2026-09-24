"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input("digite seu salario"))
if 0.00<salario<=400.00:
    aumento=salario*0.15
    novo_salario=salario+aumento
    print(f"o seu novo salário é R${novo_salario:.2f},o valor do reajuste é R${aumento}")
elif 400.01<=salario<=800.00:
    aumento=salario*0.12
    novo_salario=salario+aumento
    print(f"o seu novo salário é R${novo_salario:.2f},o valor do reajuste é R${aumento}")
elif 800.01<=salario<=1200.00:
    aumento=salario*0.10
    novo_salario=salario+aumento
    print(f"o seu novo salário é R${novo_salario:.2f},o valor do reajuste é R${aumento}")
elif 1200.01<=salario<=2000.00:
    aumento=salario*0.7
    novo_salario=salario+aumento
    print(f"o seu novo salário é R${novo_salario:.2f},o valor do reajuste é R${aumento}")
elif 2000.01<salario:
    aumento=salario*0.4
    novo_salario=salario+aumento
    print(f"o seu novo salário é R${novo_salario:.2f},o valor do reajuste é R${aumento}")

