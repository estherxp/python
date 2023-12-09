# Crie um programa que leia um nome, e mostre o primeiro e o último nome
# Saída esperada:
# Luis Felipe Tatin Vlatkovic
# Primeiro nome: Luis
# Último nome: Vlatkovic

Nome = input('Digite seu nome: ').strip()
print(Nome)

Nome = Nome.split()
print(f'Primeiro nome: {Nome[0]}')
print(f'Ultimo nome: {Nome[-1]}')