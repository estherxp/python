# Escreva um programa que leia diversos alunos,
# crie um dicionário com as notas de dele em três disciplinas: matemática, português e história.
# Em seguida, exiba a média das notas do aluno.

alunos = {}

for _ in range(3):  # Ler 3 alunos
    nome = input("Nome do aluno: ")
    notas = {
        'matematica': float(input('Nota de Matemática: ')),
        'portugues': float(input('Nota de Português: ')),
        'historia': float(input('Nota de História: '))
    }
    alunos[nome] = notas

for aluno, notas in alunos.items():
    media = sum(notas.values()) / len(notas)
    print(f'A média das notas de {aluno} é: {media:.2f}')
