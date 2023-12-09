# Crie um programa para analisar o IMC de uma pessoa,
# e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
# IMC = PESO(quilos) / Altura² (metros)
# BAIXO PESO < 18,5
# NORMAL 18,5 a 24,99
# SOBREPESO 25 a 29,99
# OBESIDADE >30

def imc(a):
    if a < 18.5:
        print('BAIXO PESO')
    elif a >= 18.5 and a <= 24.99:
        print('NORMAL')
    elif a >= 25 and a <= 29.99:
        print('SOBREPESO')
    elif a > 30:
        print('OBESIDADE')

peso = float(input('Digite seu peso KG (Ex. 62.4): '))
altura = float(input('Digite sua altura (Ex. 1.72)'))

imc_pessoa = peso / (altura*altura)

print(f'\nSeu IMC é de {imc_pessoa:.2f}'
      f'\nSeu IMC é considerado: ')

imc(imc_pessoa)