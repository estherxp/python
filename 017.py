#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

def vogal_or_consoante(a):
    if a == 'a' or a =='e' or a== 'i' or a == 'o' or a == 'u':
        print('Sua letra é uma vogal')
    else:
        print('Sua letra é uma consoante.')

Letra = input('Digite uma letra: ')
vogal_or_consoante(Letra)