#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

def vogal(a):
    if a == "a" or "e" or "i" or "o" or "u":
        print('A palavra inicia-se com uma letra vogal')
    else:
        print('A palavra inicia-se com uma letra consoante')

palavra = input("Digite uma palavra: ")

vogal(palavra[1])

if palavra[0] in 'aeiou':
    print('É vogal.')
else:
    print('É consoante.')
