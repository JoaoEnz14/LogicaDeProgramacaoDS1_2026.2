# TODO: Implemente a expressão de validação
media_aluno = float(input("Média do aluno"))
frequencia_percentual = int(input("Percentual da frequência"))

# Crie a variável aprovado com a expressão lógica
aprovado = media_aluno >= 6.0 and frequencia_percentual >= 75
print("Status de aprovação:", aprovado)
