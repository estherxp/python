#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10,
#entre 10 e 20 ou maior que 20.

def margem(a):
    if a >= 0 and a <= 10:
        print('Seu número está entre 0 e 10.')
    elif a >= 10 and a <= 20:
        print('Seu número está entre 10 e 20')
    elif a > 20:
        print('Seu número é maior de 20.')
    else:
        print('Seu número não é maior que 20 e nem está entre 0 e 20.')

n1 = float(input('Digite um número: '))
margem(n1)