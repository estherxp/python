#Jogo da Adivinhação
# - Escolha um número aleatório entre 1 e 10, depois peça ao usuário para adivinhar o número.

import random
print("Jogo de advinhação")
pc_player = random.randint(1, 10)
jogador = int(input("Tente advinhar um número entre 1  e 10:  "))

if jogador == pc_player:
    print("Você venceu!")
else:
    print(f'Não foi dessa vez o número escolhido pelo computador foi {pc_player}, Boa sorte na proxíma')



