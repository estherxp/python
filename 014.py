#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

def Positivo_or_Negativo(a):
    if a >= 0:
        print('Positivo')
    else:
        print('Negativo')
    return a

n1 = float(input('Digite um número: '))
Positivo_or_Negativo(n1)
