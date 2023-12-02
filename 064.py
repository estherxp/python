# Crie um programa onde o usuário possa digitar sete letras,
# e cadastre em uma única lista, que mantenha separado as consoantes das vogais

lista = [[], []] # lista dentro de outra lista

for i in range(0, 7):
    letra = input('Digite uma Letras: ')
    if letra in 'aeiou':
        lista[0].append(letra)
    else:
        lista[1].append(letra)

print(f'Vogais: {lista[0]}'
      f'\n Consoantes: {lista[1]}'
      f'\n A lista completa é {lista}')
