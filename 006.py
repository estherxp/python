# Escreva um programa que leia 6 notas diferentes e faça a média do aluno
# Saída esperada:
# A sua média final é : 5

print('********** Calculadora de nota média **********\n')

n1 = float(input('Digite a 1ª nota do estudante: '))
n2 = float(input('Digite a 2ª nota do estudante: '))
n3 = float(input('Digite a 3ª nota do estudante: '))
n4 = float(input('Digite a 4ª nota do estudante: '))
n5 = float(input('Digite a 5ª nota do estudante: '))
n6 = float(input('Digite a 6ª nota do estudante: '))

media = (n1 + n2 + n3 + n4 + n5 + n6) / 6

print(f'\nA sua média final é : {media}')

print('\nFinalizando aplicação...')
