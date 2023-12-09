#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

def iguais_or_diferentes(a,b):
    if a == b:
        print('Seus números são iguais.')
    else:
        print('Seus número são diferentes.')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

iguais_or_diferentes(n1, n2)