# Crie um programa que leia o nome, sexo e idade de vários Alunos,
# guardando os dados de cada aluno em um dicionário e todos os dicionários em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da média

alunos = []
total_alunos = 0
soma_idades = 0
mulheres = []
idades_acima_media = []

while True:
    nome = input('Nome do aluno (ou fim para encerrar): ')
    if nome.lower() == 'fim':
        break

    sexo = input('Sexo do aluno (M/F): ').upper()
    idade = int(input('Idade do aluno: '))

    aluno = {'nome': nome, 'sexo': sexo, 'idade': idade}
    alunos.append(aluno)

    total_alunos += 1
    soma_idades += idade

    if sexo == 'F':
        mulheres.append(nome)

media_idade = soma_idades / total_alunos

for aluno in alunos:
    if aluno['idade'] > media_idade:
        idades_acima_media.append(aluno['nome'])

print('\nResultados:')
print(f'a. Total de alunos cadastrados: {total_alunos}')
print(f'b. Média de idade do grupo: {media_idade:.2f}')
print(f'c. Lista de mulheres: {mulheres}')
print(f'd. Lista de pessoas com idade acima da média: {idades_acima_media}')
