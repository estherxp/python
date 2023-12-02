# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
# cadastrando tudo em uma lista composta
from random import randint
from time import sleep

palpitesMega = []

print('\nBem vindo ao Programa:'
      '\nGerador de palpites'
      '\npara a ** MEGA SENA!! **')
print()

qtdJogos = int(input('Quantos jogos deseja: '))

print(f'\nSorteando Valores')
print()

for contagem in range(qtdJogos):
    jogo = []
    for qtdValores in range(6):
        sorteio = randint(1, 60)

        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)

    jogo.sort()
    palpitesMega.append(jogo[:])
    print(f'Jogo {contagem + 1}: {palpitesMega[contagem]}')
    sleep(0.5)

print()
print(f'BOA SORTE!')
