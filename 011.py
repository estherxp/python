# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome

Nome = input('Digite seu nome: ').strip()

print(f'\nSeu nome é {Nome.upper()}')
print(f'Seu nome é {Nome.lower()}')

print(f'\nSeu nome possuí {len(Nome.replace(" ", ""))} letras')

Nome = Nome.split()
print(f'Seu primeiro nome possuí {len(Nome[0])} letras')


