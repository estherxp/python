#Crie um programa para jogar JOKEMPO, usando a função random.randint
import random
def cpu_player(a):
    if a == 1:
        print('PEDRA')
    elif a == 2:
        print('PAPEL')
    elif a == 3:
        print('TESOURA')
def regras_JOKEMPO(a,b):
    if a == 1 and b == 1:
        print('EMPATE')
    elif a == 1 and b == 2:
        print('PAPEL ganhou de PEDRA')
    elif a == 1 and b == 3:
        print('PEDRA ganhou de TESOURA')
    elif a == 2 and b == 1:
        print('PAPEL ganhou de PEDRA')
    elif a == 2 and b == 2:
        print('EMPATE')
    elif a == 2 and b == 3:
        print('TESOURA ganhou de PAPEL')
    elif a == 3 and b == 1:
        print('PEDRA ganhou de TESOURA')
    elif a == 3 and b == 2:
        print('TESOURA ganhou de PAPEL')
    elif a == 3 and b == 3:
        print('EMPATE')

x1 = int(input('Digite [1] para PEDRA, [2] para PAPEL e [3] para TESOURA: '))
x2 = random.randint(1,3)

print('\nPlayer 2: ')
cpu_player(x2)

print('\nResultado: ')
regras_JOKEMPO(x1,x2)
