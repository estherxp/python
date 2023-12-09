# Calculadora de Gorjeta
# Solicite ao usuário o valor da conta e a porcentagem da gorjeta que eles gostariam de dar,
# em seguida, calcule o valor total da conta incluindo a gorjeta.

print('Calculadora de Gorjeta')
valor_conta = input('Digite o valor total da conta: ')
p_escolhida = input('Digite quantos % você gostaria da gorjeta: ')

# porcentagem_gorjeta = (porc / 100)
# Gorjeta = custo do serviço * porcentagem da gorjeta.

gorjeta = (valor_conta / 100) * p_escolhida
print(f'O valor da gorjeta é de {gorjeta} reais.')
