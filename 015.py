#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar.

def par_or_impar(a):
    if a % 2 == 0:
        print('Seu número é par.')
    else:
        print('Seu número é impar.')
    return a

n1 = float(input('Digite um número: '))
par_or_impar(n1)