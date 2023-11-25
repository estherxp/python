# Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa
# lista até que ele digite um número negativo. Em seguida, exiba a lista na tela.

try:
    lista_numeros = []
    while True:
        numero = int(input('Digite um número: '))
        if numero < 0:
            break
        lista_numeros.append(numero)

except ValueError:
    print('Só aceitamos números!')
print(f"Lista de números inseridos: {lista_numeros}")

