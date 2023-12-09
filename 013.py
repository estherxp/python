# Crie um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra “a”
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece na última vez

Nome = input('Digite sua frase: ').strip()
Nome = Nome.upper()

cont_A = Nome.count('A')
print(f'\nA letra A aparece {cont_A} vezes')
pri_A = Nome.find('A')
print(f'A letra A a primeira vez na posição: {pri_A}')
ult_A = Nome.rfind('A')
print(f'A letra A aparece a última vez na posição: {ult_A}')
