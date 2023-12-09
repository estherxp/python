'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''
soma = 0
masculino = 0
feminino = 0
feminino_menos20 = 0
idade_masc_maior = 0
nome_homem_velho = 'nada'

for pessoa in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    genero = str(input('Escolha o gênero:\n [M] Masculino\n [F] Feminino\n'))

    soma_idade = soma + idade

    if genero == 'M':
        masculino = masculino + 1
        if genero == 'M' and idade > idade_masc_maior:
            nome_homem_velho = nome
            idade_masc_maior = idade


    elif genero == 'F':
        feminino = feminino + 1
        if genero == 'F' and idade <= 20:
            feminino_menos20 = feminino_menos20 + 1



    if pessoa == 4:
        idade_media = soma_idade / 4
        print(f'A idade média é {idade_media}')

        print(f'{feminino_menos20} Mulheres possuem idade igual ou inferior a 20 anos.')

        print(f'O homem mais velho é {nome_homem_velho} e possuí {idade_masc_maior} anos.')


