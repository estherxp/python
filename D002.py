'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome
OBS: Tratar os espaços extras entre os nomes
'''
Nome = input('Digite seu nome: ').strip()
Nome_s_espaco = Nome.replace(' ','')
Nome_lista = Nome.split()

Qt_letras_total = len(Nome_s_espaco)
Qt_letras_primeiro = len(Nome_lista[0])

print(f'\n{Nome.upper()}')
print(f'{Nome.lower()}')
print(f'\nO nome completo possuí {Qt_letras_total} letras')
print(f'O primeiro nome possuí {Qt_letras_primeiro} letras')
