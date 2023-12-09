#Escreva um programa que leia 10 número, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

soma = 0

for contador in range(1, 11):
    contador = int(input(f'Digite o número {contador}: '))
    if contador % 2 == 0:
        soma = soma + contador
        print(f'Soma {soma} + {contador} = {soma}')

