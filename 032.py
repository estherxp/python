#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.
n1 = int(input('Digite o intervalo inicial: '))
n2 = int(input('Digite o intervalo final: '))

for contador in range(n1, n2+1):
    if contador % 2 == 0:
        print(contador)