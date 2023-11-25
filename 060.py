# Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números pares da lista.

numeros = list(range(1,11))
numeros_pares = [num for num in numeros if num % 2 == 0]
print(f'Números Ímapres de 1 a 10: {numeros_pares}')