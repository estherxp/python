#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0

for pessoa in range(1, 8):
    peso = float(input(f'Digite o peso {pessoa}: '))

    if peso > maior:
        maior = peso
    elif peso < maior:
        menor = peso

print(f'O maior peso é {maior}\nO menor peso é {menor}')

