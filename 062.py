# Escreva um programa que crie duas listas com 5 números cada uma e exiba a
# soma dos elementos correspondentes das duas listas. Por exemplo, se as listas forem
# [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].

try:
    lista1 = [int(input('Digite números para a primeira lista: ')) for i in range(5)]
    lista2 = [int(input('Digite números para a segunda lista: ')) for i in range(5)]

    soma_elementos = [a + b for a, b in zip(lista1, lista2)]
    print(f'A soma dos elementos correspondentes são: {soma_elementos}')

except ValueError:
    print('Digite apenas números!')
