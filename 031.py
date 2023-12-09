#Escreva um programa que verifique se uma frase é um palíndromo.
'''
palavra = str(input('Digite uma palavra palindromo: '))

print(palavra)
palavra_invertida = palavra [::-1]

if palavra == palavra_invertida:
    print('É uma palavra palindromo')
else: (
        print('Não é uma palavra polindromo')
    )
'''
palavra = input('Digite uma palavra: ')

compatibilidade = 0

for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i -1]:
        compatibilidade = compatibilidade + 1

if compatibilidade == len(palavra):
    print('É palindromo.')

else:
    print('Não é.')