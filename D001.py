<<<<<<< Updated upstream:010_01_desafio.py
'''Escreva um programa que execute o cálculo da método horária da posição no MRUV,
e retorne de acordo com o tempo informado pelo usuário
Saída esperada:
A posição do objeto no tempo x é de y (m)
'''
print('********** Calculadora de MRUV **********\n')

S = float(input('Digite o valor da posição inicial de um objeto: '))
V = float(input('Digite o valor da velocidade do objeto: '))
T = float(input('Digite o valor de tempo: '))
A = float(input('Digite o valor de aceleração constante durante o movimento: '))

S_final = S + (V * T) + ((A *  T**2) / 2)

print(f'\nA posição do objeto no tempo {T} é de {S_final} (m)')

print('\nFinalizando aplicação...')
=======
'''Escreva um programa que execute o cálculo da Função horária da posição no MRUV,
e retorne de acordo com o tempo informado pelo usuário
Saída esperada:
A posição do objeto no tempo x é de y (m)
'''
print('********** Calculadora de MRUV **********\n')

S = float(input('Digite o valor da posição inicial de um objeto: '))
V = float(input('Digite o valor da velocidade do objeto: '))
T = float(input('Digite o valor de tempo: '))
A = float(input('Digite o valor de aceleração constante durante o movimento: '))

S_final = S + (V * T) + ((A *  T**2) / 2)

print(f'\nA posição do objeto no tempo {T} é de {S_final} (m)')

print('\nFinalizando aplicação...')
>>>>>>> Stashed changes:D001.py
