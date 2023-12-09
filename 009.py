# Escreva um programa que leia um tipo de dado e usando a função type(),
# retorne ao usuário, qual o tipo de dado informado
# Saída esperada:
# O dado é : <class ‘str’>

print('********** Leitor de dados string **********\n')

dado = input('Digite um dado: ')

print(f'O dado é : {type(dado)}')

print('\nFinalizando aplicação...')