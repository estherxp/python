#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

n1 = int(input('Digite um número inteiro: '))

for tabuada in range (1, 11):
    print(f'Tabuada {n1} * {tabuada} = {n1 * tabuada}')