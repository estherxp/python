# Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:
# 1 Quantas pessoas foram cadastradas
# 2 Uma listagem com as pessoas com o maior QI
# 3 Uma listagem com as pessoas de menor QI

dadosTemp, dadosPessoa = [], []
maior, menor = 0, 0

while True:
    dadosTemp.append(input('Nome: ').strip().capitalize())
    dadosTemp.append(float(input('Qi: ')))
    print('-' * 30)

    # Maior e menor qi entre os dados informados
    if len(dadosPessoa) == 0:
        maior = menor = dadosTemp[1]
    elif dadosTemp[1] > maior:
        maior = dadosTemp[1]
    elif dadosTemp[1] < menor:
        menor = dadosTemp[1]

    dadosPessoa.append(dadosTemp[:])  # Fazendo uma cópia da lista temporária para principal
    dadosTemp.clear()  # Limpando a lista temporária

    continuar = input('Continuar? [S/N]: ').strip().upper()

    # Caso usuário informe uma opção inválida
    while continuar not in ('S', 'N'):
        print('\nValor incorreto, informe a opção correta...')
        continuar = input('Continuar? [S/N]: ').strip().upper()
    print('-' * 30)

    if continuar == 'N':
        print('Encerrando o programa...')
        print('-' * 30)
        break

print(f'\nPessoas Cadastradas: {len(dadosPessoa)}'
      f'\nO Maior Qi foi: {maior} de: ', end='')
for pessoa in dadosPessoa:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end=' ')
print()

print(f'O Menor Qi foi de: {menor} de: ', end='')
for pessoa in dadosPessoa:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end=' ')
