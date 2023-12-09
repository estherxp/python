#Escreva um programa que calcule a soma dos números de 1 a 100 usando um loop
soma = 0

for contador in range(1,101):
    soma = soma + contador
    print(f'{soma} + {contador} = {soma}')