#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos)..

def maioridade(a):
    if a >= 18:
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade.')

n1 = float(input('Digite sua idade: '))
maioridade(n1)