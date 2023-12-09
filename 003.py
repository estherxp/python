# Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo,
# e retorne para o usuário
# Saída esperada:
# Seu nome completo é: xxxx

print('********** Mostrador de Nome Completo **********\n')

Nome = input('Digite seu primeiro nome ')
Sobrenome = input('Digite seu sobrenome: ')
Nome_completo = Nome + ' ' + Sobrenome

print(f'\nSeu nome completo é: {Nome_completo}')

print('\nFinalizando aplicação...')