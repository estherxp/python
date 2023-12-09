# Escreva um programa que leia um tipo de dado e usando a método .isnumeric(), retorne ao usuário
# Saída esperada:
# O dado informado é número?
# 	TRUE / FALSE

print('********** Leitor de dados INT **********\n')

dado = input('Digite um dado: ')

print(f'O dado informado é número?\n{dado.isnumeric()}')

print('\nFinalizando aplicação...')
