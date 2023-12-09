#Calculadora de IMC
# - Solicite ao usuário sua altura e peso, e calcule seu Índice de Massa Corporal (IMC).
print('----Calculadora de IMC----')
def imc(a):
    if a < 18.5:
        print('BAIXO PESO')
    elif a >= 18.5 and a <= 24.99:
        print('NORMAL')
    elif a >= 25 and a <= 29.99:
        print('SOBREPESO')
    elif a > 30:
        print('OBESIDADE')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc_pessoa = peso / (altura*altura)

print(f'\nSeu IMC é de {imc_pessoa:.2f}'
      f'seu IMC é considerado: ')
imc(imc_pessoa)
